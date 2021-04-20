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
pip install .
```

## Usage
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

This wrapper runs within the context management protocol meaning it
will automatically perform teardown (logout) once your code leaves
the scope of the with statement. In order to access wrapper methods
in other functions pass the object returned by the with statement to
your function, for example:
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
    vmr.inputs[1].A3 = False
    print(f'Output A4 of Strip {vmr.inputs[1].label}: {vmr.inputs[1].A3}')

def do_other_things(vmr):
    # Set the gain slider of the leftmost output bus
    vmr.outputs[0].gain = -6.0
    print(vmr.outputs[0].gain)
    vmr.outputs[0].gain = 3.0
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

#### `voicemeeter.remote(kind_id, delay: float=.001, mdelay: float=.005, max_polls: int=4) -> 'instanceof(VMRemote)'`
Factory function for remotes. 
- delay applies to parameter getters 
- mdelay applies to macrobutton getter
- max_polls defines the number of times pdirty and mdirty parameters are polled

Occasionally it requires more than a single poll to determine whether parameters have been updated. The wrapper passes 1000 unit test runs
cleanly with default values but if you wish to alter these settings you may do so with argument variables to voicemeeter.remote.

Returns a `VMRemote` based on the `kind_id`.  
Use it with a context manager
```python
with voicemeeter.remote('potato') as vmr:
    vmr.inputs[0].mute = True
```

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
#### `vmr.button_state(id, state)`
Set the state and execute the script for macrobutton by id
#### `vmr.button_stateonly(id, state)`
Set the current state but don't execute the script for the macrobutton by id
#### `vmr.button_trigger(id, state)`
Set trigger status for macrobutton by id
- `id`: int, from 0 to 69
- `state`: boolean

Example:
```python
  # set macrobutton id 34 state to 1
  vmr.button_state(34, 1)
  # set macrobutton id 10 stateonly to 0  
  vmr.button_stateonly(10, 0)
  # set macrobutton id 17 trigger to 1  
  vmr.button_trigger(17, 1)
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

  # Filepath must be a raw string (or escaped backslashes)
  recorder.load(Filepath)
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

## Resources
- [Voicemeeter Remote C API](https://forum.vb-audio.com/viewtopic.php?f=8&t=346)
