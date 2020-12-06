*****************************
A small Intro to openhiven.py
*****************************

.. highlight:: python

Welcome to the Documentation of openhiven.py!

Openhiven.py is an easy, open-source and async API wrapper written in Python
that provides basic functionality for the Hiven Swarm and API.

.. note::
    The openhiven.py Library is written entirely async and needs
    to be run in an asyncio-environment!

    For more info about asyncio: `Asyncio documentation <https://docs.python.org/3/library/asyncio.html>`_

Environment
~~~~~~~~~~~

    To use openhiven.py Python >= 3.7 currently is recommended, but version 3.6 and lower can be used but stable performance cannot be guaranteed!
    Python 2 is entirely not supported, and currently, there is no plan to make openhiven.py available for Python 2 since many features are dependent on Python 3 and the modern async module of Python 3!


Installation
~~~~~~~~~~~~

    **PyPi Installation:**
    .. code-block:: none
        python3 -m pip install -U openhivenpy

    **Github Build:**

    `Not recommended since the build can be unstable`
    .. code-block:: none
        python -m pip install -U https://github.com/FrostbyteSpace/openhiven.py/archive/main.zip


Basic Concept
~~~~~~~~~~~~~

    The system of openhiven.py is very closely related to the discord.py module and was structured to be similar to it. Therefore, the 
    basic concept is based on an event listener system that can register events and executes them when a Hiven Swarm Event is received. 
    That process gets handled over the integrated `Event Handler <https://openhivenpy.readthedocs.io/en/latest/>`_ class.

    .. note:: 
        The Default Event Handler can get modified by passing a custom class to the HivenClient.
        For more information see `Event Handler <https://openhivenpy.readthedocs.io/en/latest/>`_ 


Logging and Debugging
~~~~~~~~~~~~~~~~~~~~~

    Openhiven.py uses to detect issues and problems the built-in `logging <https://docs.python.org/3/library/logging.html#module-logging>`_ module of Python.
    That module can provide easy logging features and customization of program logging.

    In the case of openhiven.py it is used to print out events, errors and show what is executed in the program.

    **Simple Example of logging:**
    .. code-block:: python
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

    **Extended Example of logging for debugging:**
    .. code-block:: python
        import logging
        import openhivenpy

        logger = logging.getLogger("openhivenpy")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='openhiven.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

    For more customization for the :code:`logging.Formatter <https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial>`_ and :code:`logging.FileHandler <https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial>`_ class visit the `logging <https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial>`_ documentation!