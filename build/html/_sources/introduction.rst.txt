*****************************
A small Intro to openhiven.py
*****************************

.. highlight:: python

Welcome to the Documentation of openhiven.py!

openhiven.py is an easy, open-source and async API wrapper written in Python
that provides basic functionality for the Hiven Swarm and API.

.. note::
    The openhiven.py Library is therefore written entirely async and can
    only be used with asyncio programs! 

    For more info about asyncio look into the `Asyncio docs <https://docs.python.org/3/library/asyncio.html>`_

Environment
~~~~~~~~~~~

    To use openhiven.py Python >= 3.7 currently is recommended, but not needed! 


Installation
~~~~~~~~~~~~

    **PyPi Installation:**::
        python3 -m pip install -U openhivenpy

    **Github Build:**

    `Not recommended since the build can be unstable`::
        python -m pip install -U https://github.com/FrostbyteSpace/openhiven.py/archive/main.zip


Basic Concept
~~~~~~~~~~~~~

    The system of openhiven.py is very closely related to the discord.py module and was structured to be similar to it.
    The basic concept therefore is based on a event listener system that can register events and executes them when a Websocket event
    gets triggered!

    That process gets handled over the integrated `Event Handler <https://openhivenpy.readthedocs.io/en/latest/>`_ class
    which triggers and executes the events if they are found in the client.

    .. note:: 
        The Default Event Handler can theoretically get customized and modified to handle events
        with even better performance. See `Event Handler <https://openhivenpy.readthedocs.io/en/latest/>`_ for more information


Logging and Debugging
~~~~~~~~~~~~~~~~~~~~~

    openhiven.py uses to detect issues and problems the built-in `logging <https://docs.python.org/3/library/logging.html#module-logging>`_ module of Python.
    That module can provide easy logging features and customization of program logging.

    In the case of openhiven.py it is used to print out events, errors and show what is executed in the program.

    **Simple Example of logging:**::
        import logging

        logging.basicConfig(level=logging.INFO)


    That code snippet appended at the beginning of the file will print out basic info about the program as well as errors.

    .. Note::
        This code snippet will activate logging for all modules available!
        If other modules with logging are important this will also active their logging output!

    The available options for logging options are :code:`CRITICAL`, :code:`ERROR`, :code:`WARNING`, :code:`INFO`, and :code:`DEBUG`.

    The base concept of logging is that certain events have different importance levels and
    based on the user-specified logging level they are going to be printed out on the Console or stored
    in a `.log` file.

    For more advanced usage of logging and also debugging it is recommended to use the :code:`logging.getLogger("openhivenpy")` and
    specify the way the log should be handled! That can be extended to the basic logging to print out logs and save them to a file!

    **Extended Example of loggign for debugging:**::
        import logging
        import openhivenpy

        logger = logging.getLogger("openhivenpy")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='openhiven.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)


    For more customization for the :code:`logging.Formatter` and :code:`logging.FileHandler` class visit the `logging <https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial>`_ documentation!