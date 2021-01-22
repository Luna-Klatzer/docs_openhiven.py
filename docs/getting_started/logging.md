# Logging and Debugging

---

OpenHiven.py uses to log and report issues and problems the built-in
[logging](https://docs.python.org/3/library/logging.html#module-logging) module of Python.
That module can provide easy logging features and customization of program logging.

The module logging is based on multiple levels of importance that specified on the user input will
log issues lower that level.

The available levels for logging are:

| Levels | Description |
| ----------- | ----------- |
| DEBUG | Logs every output related to the running program |
| INFO | Logs only vital information about the program | 
| WARNING | Logs warnings and errors in the program | 
| ERROR | Logging is strictly restricted to errors | 
| CRITICAL | Only if the program fails critically an error should be reported | 


### Simple Example of logging

The code snippet will activate all logging in the range of the program. That means imported modules would also log
their information if they have logging used in their module.

```
import logging

logging.basicConfig(level=logging.INFO)
```

The resulting log of the prior example would look like this:

```
INFO:openhivenpy.gateway.http:[HTTP] Session was successfully created!
INFO:openhivenpy.gateway.ws:[WEBSOCKET] >> Authorizing with token
INFO:openhivenpy.gateway.ws:[WEBSOCKET] << Connection to Hiven Swarm established
INFO:openhivenpy.gateway.ws:[WEBSOCKET] >> Initialization of Client was successful!
INFO:openhivenpy.types.hiven_client:[CLIENT] Client loaded all data and is ready for usage!
```

Here, the initialization was successful, and the HivenClient connected itself to Hiven and logged no errors. With the
level 'INFO' that is used here. Only the vital information was logged, while with 'DEBUG' the HivenClient would
activate a broader range of useful logs for debugging. Mostly websocket Message data and HTTP requests that are
needed to start the client. 

### Usage of INFO and DEBUG
'DEBUG' is excellent for detecting issues in the program and also seeing how
OpenHiven.py works in the  background. 'INFO' is, on the other hand, handy for deployment and usage where the
HivenClient should log only errors.

For more advanced usage of logging and also debugging it is recommended to use a more advanced logging system
to get timestamps, logging info and user data that are connected to the running of the Bot.

### Advanced Logging:

```python
import logging
import openhivenpy

logger = logging.getLogger("openhivenpy")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='openhiven.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
```

With this example, also time will be logged, and the log will even be saved to a file called `openhiven.log`.

For more customization for the `logging.Formatter` and `logging.FileHandler` classes
visit the [logging](https://docs.python.org/3/library/logging.html#module-logging) documentation!