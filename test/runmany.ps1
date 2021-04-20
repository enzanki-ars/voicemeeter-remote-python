param(
        [parameter(Mandatory=$false)]
        [Int] $num = 1,
        [switch]$cycle,
        [switch]$Log
        )

$global:failures = 0

Function RunTests {
        param([int]$cycle_num)
        if ($cycle_num) {
                $num = $cycle_num
        }

        $logfile = "nosetest.log"
        $failures = $global:failures
        $firstrun = $false

        if ($cycle_num -eq 100) { $firstrun = $true }

        (Get-Content '__init__.py') | ForEach-Object {
                $m = [regex]::Match($_, '^(DELAY)\s=\s(\d.\d+)')
                if ($m.captures.groups.count -gt 1) {
                        $delay = $m.captures.groups[2]
                }
                $m2 = [regex]::Match($_, '^(MDELAY)\s=\s(\d.\d+)')
                if ($m2.captures.groups.count -gt 1) {
                        $mdelay = $m2.captures.groups[2]
                }
                $m3 = [regex]::Match($_, '^(MAX_POLLS)\s=\s(\d+)')
                if ($m3.captures.groups.count -gt 1) {
                        $maxpolls = $m3.captures.groups[2]
                }
        }

        1..$num | ForEach-Object { `
                if ($Log) { "Running test $_ of ${num} runs"  | Tee-Object -FilePath $logfile -Append } 
                else { Write-Host "Running test $_ of ${num} runs" }

                ForEach ($line in $(Invoke-Expression "nosetests --randomize -s test 2>&1")) { 
                        if ($Log) {
                                if ($line -NotMatch '^(System)') { 
                                "${line}" | Tee-Object -FilePath $logfile -Append 
                                }
                        } else {
                                if ($line -NotMatch '^(System)') { Write-Host "${line}" }
                        }        

                        $m = [regex]::Match($line, '^(FAILED)\s\(failures=(\d+)\)')
                        if ($m.captures.groups.count -gt 1) {
                                $failures += $m.captures.groups[2].value           
                        }
                }
        }

        if ($Log) {
                $log_backup = LogRotate -logfile $logfile
                $log_backupfile = Split-Path $log_backup -leaf

                $summary_file = "summary.log"
                if ($firstrun -eq $true) {
                "==========================================================`n" + `
                "NOTES:" | Tee-Object -FilePath $summary_file -Append
                }
                "==========================================================`n" + `
                "${num} test run with ${delay} delay, ${mdelay} mdelay and ${maxpolls} max_polls`n" + `
                "Total failures: ${failures}`n" + `
                "Logfile for this test run: ${log_backupfile}`n" + `
                "==========================================================" | `
                Tee-Object -FilePath $summary_file -Append
        } else {
                "==========================================================",
                "${num} test run with ${delay} delay, ${mdelay} mdelay and ${maxpolls} max_polls",
                "Total failures: ${failures}",
                "==========================================================" | Write-Host
        }
        $global:failures = $failures
}

Function LogRotate {
        param([string]$logfile)
        Get-ChildItem ./ -recurse `
        | Where-Object {$_.basename -ne 'summary' -and $_.extension -eq ".log" } `
        | ForEach-Object {
                $i = 1
                $StopLoop = $false

                do {
                        try {
                                $savefile = "$($_.Fullname)_$i.backup"
                                Rename-Item -Path $_.FullName `
                                -NewName $savefile -ErrorAction "Stop"

                                $StopLoop = $true
                        }
                        catch {
                                Start-Sleep -m 100
                                $i++
                        }      
                } until ($StopLoop -eq $true)
        }
        $savefile
}

if ($MyInvocation.InvocationName -ne ".")
{
        & '..\venv_macros\Scripts\activate.ps1'

        if ($cycle) {
                @(100, 200, 500, 1000) | ForEach-Object {
                        RunTests -cycle_num $_
                        if ($global:failures -gt 0) { break }
                }
        } else { RunTests }

        & 'deactivate'
}
