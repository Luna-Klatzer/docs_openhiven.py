.. _introduction:

*****************************
A small Intro to openhiven.py
*****************************

.. highlight:: python

Welcome to the Documentation of openhiven.py!

openhiven.py is an easy, fast and async API wrapper written in Python
that provides extensive functionality for the Hiven Swarm and Hiven API.

.. note::
    The openhiven.py module is entirely written in async and can therefore only be used in an
    async event loop and environment. For more info about asyncio look into the
    `Asyncio documentation <https://docs.python.org/3/library/asyncio.html>`_

Environment
~~~~~~~~~~~

    To use openhiven.py Python >= 3.6 is required since the package aiohttp needs Python
    functionality which is only available in Python >= 3.6!
    Python 2 is entirely not supported, and currently, there is no plan to make openhiven.py available for Python 2,
    since many features are dependent on Python 3 and the modern async module of Python 3 as well as aiohttp!


Installation
~~~~~~~~~~~~

    **PyPi Installation:**

    .. code-block:: python

        python3 -m pip install -U openhivenpy

    **Specific Version:**

    .. code-block:: python

        python3 -m pip install -U openhivenpy==0.1.1.2

    **Github Build:**

    `Not recommended since the build can be unstable`

    .. code-block:: python

        python -m pip install -U https://github.com/FrostbyteSpace/openhiven.py/archive/main.zip


Basic Concept
~~~~~~~~~~~~~

    The system of openhiven.py is very closely related to the discord.py(Discord Python Wrapper) module and
    was structured to be similar to it. Therefore, the basic concept is based on an event listener system where events
    are mapped to user-specified functions and methods. These will be executed when a Hiven Swarm Event is received,
    enabling the user to customise the event's handling!

    An Hiven event in this context is an addition, change or removal of data on Hiven. The data which is changed will
    then be passed as arguments to the functions which can then be accessed and used for further interaction with
    the Hiven API.

    Basic Hiven Event Listener that listens for messages and prints out their content:
    
    .. code-block:: python

        import openhivenpy as hiven

        client = hiven.UserClient("Insert token")

        @client.event()
        async def on_message_create(msg):
            print(msg.content)

        client.run()


    The event system and handling is done over the integrated
    `Event Handler <https://openhivenpy.readthedocs.io/en/latest/>`_ class, which defaults to the used HivenClient itself.
    Async Functions that are tagged with the `@client.event()` decorator will automatically be saved in the EventHandler
    and then called whenever an Event is triggered.

    Class methods can also be registered for event listening, but it is recommended to use a class which inherits the
    HivenClient, making the Event listener directly find the methods when needed without needing the methods to be registered.

    Example of an inherited HivenClient:

    .. code-block:: python

        import openhivenpy as hiven
        import logging

        logging.basicConfig(level=logging.INFO)


        class Bot(hiven.UserClient):
            def __init__(self, token):
                self._token = token
                super().__init__(token)

            # Not directly needed but protects the token from ever being changed!
            @property
            def token(self):
                return self._token

            # Methods can be defined directly in the class without the need of the decorator
            async def on_ready(self):
                print("Bot is ready!")


        if __name__ == '__main__':
            client = Bot(token="Insert token")
            client.run()


    .. note:: 
        The Default Event Handler can get modified by passing a custom one to the HivenClient.
        For more information see `Event Handler <https://openhivenpy.readthedocs.io/en/latest/>`_ 

    With the event system, there is also the data model system of openhiven.py. This system is a structure of many
    objects representing a Hiven object, such as a House or User which implement the data received from Hiven making
    them available in object/class form for users. These data models can directly modify and interact with the
    corresponding Hiven Object on Hiven and the Hiven API.

    For detailed documentation see `Data Models <https://openhivenpy.readthedocs.io/en/latest/>`_


Logging and Debugging
~~~~~~~~~~~~~~~~~~~~~

    openhiven.py uses to log and report issues and problems the built-in
    `logging <https://docs.python.org/3/library/logging.html#module-logging>`_ module of Python.
    That module can provide easy logging features and customization of program logging.

    The module logging is based on multiple levels of importance that specified on the user input will
    log issues lower that level.

    The available levels for logging are:

    * :code:`DEBUG`
    * :code:`INFO`
    * :code:`WARNING`
    * :code:`ERROR`
    * :code:`CRITICAL`

    **Simple Example of logging:**
    
    .. code-block:: python

        import logging

        logging.basicConfig(level=logging.INFO)

    .. note::

        The code snippet will activate logging for all modules available in the running scope!

    The resulting log will then look like this:

    **Example Log Output:**

    .. code-block:: none

        INFO:openhivenpy.gateway.http:[HTTP] Session was successfully created!
        INFO:openhivenpy.gateway.ws:[WEBSOCKET] >> Authorizing with token
        INFO:openhivenpy.gateway.ws:[WEBSOCKET] << Connection to Hiven Swarm established
        INFO:openhivenpy.gateway.ws:[WEBSOCKET] >> Initialization of Client was successful!
        INFO:openhivenpy.types.hiven_client:[CLIENT] Client loaded all data and is ready for usage!

    In this example, the initialization was successful, and the HivenClient registered and logged no errors. With the
    level 'INFO' that is used here. Only the vital information was logged, while with 'DEBUG' the HivenClient would
    activate a broader range of useful logs for debugging. Mostly websocket Message data and HTTP requests that are
    needed to start the client. 'DEBUG' is excellent for detecting issues in the program and also seeing how
    openhiven.py works in the  background. 'INFO' is, on the other hand, handy for deployment and usage where the
    HivenClient should log only errors.

    For more advanced usage of logging and also debugging it is recommended to use a more advanced logging system
    to get timestamps, logging info and user data that are connected to the running of the Bot.

    **Example for a advanced logging system:**
    
    .. code-block:: python

        import logging
        import openhivenpy

        logger = logging.getLogger("openhivenpy")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='openhiven.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

    With this example, also time will be logged and the log will even be saved to a file called `openhiven.log`.

    For more customization for the :code:`logging.Formatter` and :code:`logging.FileHandler` classes
    visit the `logging <https://docs.python.org/3/library/logging.html#module-logging>`_ documentation!

