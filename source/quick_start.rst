.. _quick_start:

***********
Quick Start
***********

.. highlight:: python

.. _event_system:

============
Event System
============

    To easily start programming with Openhiven.py the core system of Event Handling must be understood.
    This system controls the core functionality and provides the ability to interact with Hiven
    and reacting to Events that were triggered on Hiven. These events can be either that a message was sent,
    a user changed their name or that a user joined a house.

    Based on these events you can register Event Listeners that will react to these events:

    Example with on_message:

    .. code-block:: python

        import openhivenpy

        client = openhivenpy.UserClient("Insert token")

        @client.event()
        async def on_message_create(msg):
            print(msg.content)

        client.run()

    With the event listener :class:`on_message_create()` the function will be called whenever a message was created
    in your visibility. That means messages in houses you are not a member of, will not be affected by that listener.

    With that listener a :ref:`message` object will be passed to provide the option to interact and access the data
    of the message that was sent on Hiven.

    For more info of :ref:`event_handling` and the :ref:`event_handler` read the complete documentation of their functionality.

.. _simple_bot:

============
A simple Bot
============

    Using the event listeners you can build a simple bot that can listen to commands using :class:`on_message_create()`.

    In this case a simple Self-Bot or User-Bot is used. That means a account on Hiven will be overtaken and the
    program will be able to interact as such user. To use a bot account please notice that in the current version v0.1
    Bot account are only partially supported, but they can be used using the :ref:`BotClient` class.

    .. code-block:: python

        import openhivenpy

        client = openhivenpy.UserClient("Insert token")

        @client.event()
        async def on_ready():
            print("Bot is ready")

        @client.event()
        async def on_message_create(msg):
            if msg.content.startswith("!ping"):
                await message.room.send("pong")

        client.run()

    In this case the event listener :class:`on_ready` is also defined, which will be called when the Bot is ready for
    use and all data was received. Similar to :class:`on_ready`, :class:`on_init` is also available which will be called
    when the connection to Hiven was established.

    .. note::
        :class:`on_init` only means the init event from Hiven was received but no data is initialized. As such it
        cannot be used to interact with Hiven yet but execute startup methods that should as soon as possible
        be executed and available for use.

