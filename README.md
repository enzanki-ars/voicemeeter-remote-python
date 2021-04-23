# Voicemeeter Remote
A Python API to [Voicemeeter](https://www.vb-audio.com/Voicemeeter/potato.htm), a virtual audio mixer for Windows.

This work-in-progress package wraps the [Voicemeeter Remote C API](https://forum.vb-audio.com/viewtopic.php?f=8&t=346) and provides a higher-level interface for developers.

Tested against
- Basic 1.0.7.8
- Banana 2.0.5.8
- Potato 3.0.1.8


## Prerequisites
- Voicemeeter 1 (Basic), 2 (Banana) or 3 (Potato)
- Python 3.6+

## Installation
```
git clone https://github.com/Freemanium/voicemeeter-remote-python
cd voicemeeter-remote-python
```

Just the wrapper:
```
pip install .
```

With development dependencies:
```
pip install -e .['development']
```

## Usage
Use this wrapper with a context manager, for example:

### Example 1
```python
import voicemeeter

# Can be 'basic', 'banana' or 'potato'
kind = 'potato'

# Ensure that Voicemeeter is launched
voicemeeter.launch(kind)

with voicemeeter.remote(kind) as vmr:
    # Set the mapping of the second input strip
    vmr.inputs[1].A4 = True
    print(f'Output A4 of Strip {vmr.inputs[1].label}: {vmr.inputs[1].A4}')

    # Set the gain slider of the leftmost output bus
    vmr.outputs[0].gain = -6.0

    # Also supports assignment through a dict
    vmr.apply({
        'in-5': dict(A1=True, B1=True, gain=-6.0),
        'out-2': dict(mute=True)
    })

    # Resets all UI elements to a base profile
    vmr.reset()
```

Once your code leaves the scope of the with statement logout will be called
automatically. In order to separate logic into other functions pass the object
returned by with to your function, for example:

### Example 2
```python
import voicemeeter

# Can be 'basic', 'banana' or 'potato'
kind = 'potato'

# Ensure that Voicemeeter is launched
voicemeeter.launch(kind)

def do_things(vmr):
    # Set the mapping of the second input strip
    vmr.inputs[1].A3 = True
    print(f'Output A4 of Strip {vmr.inputs[1].label}: {vmr.inputs[1].A3}')

def do_other_things(vmr):
    # Set the gain slider of the leftmost output bus
    vmr.outputs[0].gain = -6.0
    print(vmr.outputs[0].gain)

with voicemeeter.remote(kind) as vmr:
    do_things(vmr)
    do_other_things(vmr)
```

## Profiles
Profiles through config files are supported.
```
mkdir profiles
mkdir profiles/potato
touch profiles/potato/mySetup.toml
```

A config can contain any key that `remote.apply()` would accept. Additionally, `extends` can be provided to inherit from another profile. Two profiles are available by default:
- `blank`, all inputs off and all sliders to `0.0`
- `base`, all physical inputs to `A1`, all virtual inputs to `B1`, all sliders to `0.0`

Sample `mySetup.toml`
```toml
extends = 'base'
[in-0]
mute = 1

[in-5]
A1 = 0
A2 = 1
A4 = 1
gain = 0.0

[in-6]
A1 = 0
A2 = 1
A4 = 1
gain = 0.0
```

## API
### Kinds
A *kind* specifies a major Voicemeeter version. Currently this encompasses
- `basic`: [Voicemeeter](https://www.vb-audio.com/Voicemeeter/index.htm)
- `banana`: [Voicemeeter Banana](https://www.vb-audio.com/Voicemeeter/banana.htm)
- `potato`: [Voicemeeter Potato](https://www.vb-audio.com/Voicemeeter/potato.htm)

#### `voicemeeter.launch(kind_id, delay=1)`
Launches Voicemeeter. If Voicemeeter is already launched, it is brought to the front. Wait for `delay` seconds after a launch is dispatched.

#### `voicemeeter.remote(kind_id, delay: float=.001, max_polls: int=5) -> 'instanceof(VMRemote)'`
Factory function for remotes.
- delay: interval between polls
- max_polls: maximum number of times a dirty parameter is polled.

max_polls define the number of times dirty parameters are polled separated by a given delay interval. Since the time taken for the Voicemeeter background service to update the polling parameters varies this allows for a quicker response time up to a max delay.

The wrapper passes 1000 unit test runs cleanly with default values but if you wish to alter these settings you may do so with argument variables to voicemeeter.remote.
If changing either argument be aware that max delay on getters is defined as the product of delay and max_polls.

Setters and polling functions run without any delay.

### `VMRemote` (higher level)
#### `vmr.type`
The kind of the Voicemeeter instance.

#### `vmr.version`
A tuple of the form `(v1, v2, v3, v4)`.

#### `vmr.inputs`
An `InputStrip` tuple, containing both physical and virtual.
#### `vmr.outputs`
An `OutputBus` tuple, containing both physical and virtual.

#### `vmr.show()`
Shows Voicemeeter if it's minimized. No effect otherwise.
#### `vmr.shutdown()`
Closes Voicemeeter.
#### `vmr.restart()`
Restarts Voicemeeter's audio engine.

#### `vmr.apply(mapping)`
Updates values through a dict.  
Example:
```python
vmr.apply({
    'in-5': dict(A1=True, B1=True, gain=-6.0),
    'out-2': dict(mute=True)
  })
```
#### `vmr.apply_profile(profile_name)`
Loads a profile.
#### `vmr.reset()`
Resets everything to the `base` profile.

### `InputStrip`
Any property is gettable and settable.
- `label`: string
- `solo`: boolean
- `mute`: boolean
- `gain`: float, from -60.0 to 12.0
- `comp`: float, from 0.0 to 10.0
- `gate`: float, from 0.0 to 10.0
- Output mapping (e.g. `A1`, `B3`, etc.): boolean, depends on the Voicemeeter kind
- `apply()`: Works similar to `vmr.apply()`
### `OutputBus`
Any property is gettable and settable.
- `mute`: boolean
- `eq`: boolean
- `gain`: float, from -60.0 to 12.0
- `apply()`: Works similar to `vmr.apply()`

### `Macrobuttons`
Can be configured using three different modes: state, stateonly and trigger
#### `vmr.button[id].state`
Set the state and execute the script for macrobutton by id
#### `vmr.button[id].stateonly`
Set the current state but don't execute the script for the macrobutton by id
#### `vmr.button[id].trigger`
Set trigger status for macrobutton by id
- `id`: int, from 0 to 69
- `state`: boolean

Example:
```python
  # set macrobutton id=34, mode=state to True
  vmr.button[34].state = True
  # set macrobutton id=10, mode=stateonly to False
  vmr.button[10].stateonly = False
  # set macrobutton id=17, mode=trigger to True
  vmr.button[17].trigger = True
```

### `Recorder`
Example:
```python
  vmr.recorder.play()
  vmr.recorder.stop()
  vmr.recorder.pause()

  # record, fw and rw until stopped
  vmr.recorder.record()
  vmr.recorder.ff()
  vmr.recorder.rw()

  # Enable loop play on
  vmr.recorder.loop()

  # Set recorder output channels
  recorder.output(A1, 1)
  recorder.output(B2, 0)

  # filepath must be a raw string (or escaped backslashes)
  recorder.load(filepath)
```

### `VMRemote` (lower level)
#### `vmr.pdirty`
`True` if UI parameters have been updated. Use this if to poll for UI updates.
#### `vmr.mdirty`
`True` if macrobutton parameters have been updated. Use this if to poll for MB updates.

#### `vmr.get(param_name, string=False)`
Calls the C API's parameter getters, `GetParameterFloat` or `GetParameterStringW` respectively. Tries to cache the value on the first call and updates the cached value if `vmr.dirty` is `True`.

#### `vmr.set(param_name, value)`
Calls the C API's parameter setters, `SetParameterFloat` or `SetParameterStringW` respectively.

### Errors
- `errors.VMRError`: Base Voicemeeter Remote error class.
- `errors.VMRDriverError`: Raised when a C API function returns an unexpected value.

### Tests
First make sure you installed the [development dependencies]https://github.com/onyx-and-iris/voicemeeter-remote-python#installation

Isolate tests using the `@nottest` decorator before each test class.

To run the tests from test directory:

`nosetests --r test` or `.\runmany.ps1 <num>` where num is the number of tests you wish to run.

If using runmany to run tests output will be logged and a summary log will be written.

For testing timing tolerances for delay and max_polls edit the values in test/\_\_init\_\_.py

## Resources
- [Voicemeeter Remote C API](https://forum.vb-audio.com/viewtopic.php?f=8&t=346)
