# Engines

SaltStack engines are fun to play with.
You can use them to have the salt-master start and restart your code either as long running procesess or have them being executed periodically.

# Requirements

There are two things required for an engine

* An engine configuration
* An engine

# Engine configuration

 In `/etc/salt/master.d/engines.conf` you would add your engine configuration and for the below minimal engine example such a config would look like this
 
 ```yaml
 engines:
   - minimal
 ```

# Minimal engine

Filename: `_engines/minimal.py`

```python
def start():
    pass
```

The above code is the minimum amount of code you need to write in order to create an engine. This engine will be started periodically (I've seen every 10 seconds) by the salt-master process.

# Engine arguments

An engine has access to the `__opts__` dictionary which can be used to get whatever config value you require.
An engine also supports arguments if you specify them as parameters to the start method.

```python
def start(name=None):
  pass
```

If your config looks like this

```yaml
engines:
  - minimal
```

then the `name` parameter will be None.
If your config looks like this

```yaml
engines:
  - minimal:
    name: minimal
```

then the `name`parameter will contain `minimal`.

# Long running engines

You can create a simple long running engine by having it run an endless loop.

```python
import time

def start():
  while True:
    time.sleep(1)
```

# Listening to the event bus

You can have your engine listen to events on the event bus using something like this

```python
def start():
    with salt.utils.event.get_event(
        "master",
        sock_dir=__opts__["sock_dir"],
        transport=__opts__["transport"],
        opts=__opts__,
    ) as event_bus:
        while True:
            event = event_bus.get_event(full=True)
            # do something with the event
```
