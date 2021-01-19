******
Client
******

Main objects used to connect to Hiven and wrap the Swarm and API

.. role:: raw-html(raw)
    :format: html

.. _Start:

===========
HivenClient
===========

    .. py:class:: HivenClient(token, *, event_loop, kwargs**)

        Main Class used to interact with the Websocket and the Hiven API.
        Inherited by :ref:`BotClient<BotClient>` and :ref:`UserClient<UserClient>`

        :param str token: Token for the interaction with Hiven.
        :param bool restart: If set to True will automatically restart the websocket once if
                             an error occurred while running. Defaults to :class:`False`
        :param str client_type:  Automatically set if UserClient or BotClient is used.
                                 Defaults to `bot`
        :param event_handler: Event Handler Class that will be used to trigger events!
                              Creates a new EventHandler on Default
        :type event_handler: :class:`openhivenpy.events.EventHandler`
        :param int heartbeat: Heartbeat interval for sending a lifesignal to Hiven.
                              Defaults to :class:`30000` (in milliseconds)
        :param bool log_ws_output: If set to :class:`True`, the websocket will log automatically
                                   all incoming json data. Can provide even more insight to the
                                   Hiven Swarm. Defaults to :class:`False`
        :param int close_timeout: Seconds after the websocket will timeout after the handshake
                                  didn't complete successfully. Defaults to :class:`40`

        :param event_loop: Event Loop that will be used for running the client and it's methods
                           Uses `asyncio.get_event_loop()` to fetch the current event_loop. Creates a new one
                           if no existing is found!
        :type event_loop: :class:`asyncio.AbstractEventLoop`

        :raises InvalidClientType: If a faulty Client Type was passed!
        :raises InvalidToken: If an empty, faulty or None Type Token was passed!
        :raises ImportError: If an required module is missing and not installed!

        .. py:function:: run()

            Starts the HivenClient and the HTTP and Swarm Connection to Hiven. Uses :class:`asyncio.get_event_loop()`
            to fetch the current event_loop. Creates a new one if no one is found!

            Wraps the :ref:`connect()<connect>` coroutine.

            .. _connect:

        .. py:function:: connect()

            Starts the HivenClient and the Websocket Connection to Hiven

            :async:

        .. py:function:: stop()

            Stops the current session if an active connection exists

            :async:

        .. attribute:: token

            Token used to connect to Hiven

            :type: str
            :value: None

        .. attribute:: open

            If :class: `True` connection is open

            :type: bool
            :value: False

        .. attribute:: closed

            Counter attribute to open

            If :class:`True` connection is closed

            :type: bool
            :value: True

        .. attribute:: user

            The user instance of the connected client.

            If not initialised the client will default to a empty object!

            :type: :class:`openhivenpy.types.Client`
            :value: object

        .. attribute:: ready

            If :class:`True` the client has received all data from Hiven and is ready for use

            :type: bool
            :value: False

        .. attribute:: initialized

            If :class:`True` the Websocket and HTTPClient are connected and running. Initialized is not ready!
            :type: bool
            :value: False

        .. attribute:: http

            HTTP-Client used for requests to Hiven.

            Can be used to execute manual requests.
            See `HTTPClient <https://openhivenpy.readthedocs.io/en/stable/advanced_usage/http_client.html>`_ for more info

            :type: :class:`openhivenpy.gateway.HTTPClient`
            :value: None

        .. attribute:: client_type

            Type of the used Client. Defaults to :class:`bot` if HivenClient is used directly

            Can be either :class:`bot` or :class:`user`

            Is None if the client wasn't initialised yet!

            :type: str
            :value: None

        .. attribute:: heartbeat

            Heartbeat of the Websocket

            :type: int
            :value: 30000

        .. attribute:: connection_status

            Connection Status of the Client

            Can be either :class:`OPENING`, :class:`OPEN`, :class:`CLOSING` or :class:`CLOSED`

            :type: str
            :value: CLOSED

        .. attribute:: websocket

            Websocket object that is used connecting to Hiven

            :type: :class:`openhivenpy.gateway.Websocket`
            :value: None

        .. attribute:: startup_time

            Time that it took the client to started

            :type: int
            :value: None

=========
BotClient
=========

    .. py:class:: BotClient(token, *, event_loop, kwargs**)

        Bot Client Class used for bot accounts that are registered on Hiven.

        .. note::
            The Bot Client is currently not entirely optimised for all API Features!
            Please report errors or missing features that need to be implemented!

        :param str token: Token for the interaction with Hiven.
        :param bool restart: If set to True will automatically restart the websocket once if
                             an error occurred while running. Defaults to :class:`False`
        :param str client_type:  Automatically set if UserClient or BotClient is used.
                                 Defaults to `bot`
        :param event_handler: Event Handler Class that will be used to trigger events!
                              Creates a new EventHandler on Default
        :type event_handler: :class:`openhivenpy.events.EventHandler`
        :param int heartbeat: Heartbeat interval for sending a lifesignal to Hiven.
                              Defaults to :class:`30000` (in milliseconds)
        :param bool log_ws_output: If set to :class:`True`, the websocket will log automatically
                                   all incoming json data. Can provide even more insight to the
                                   Hiven Swarm. Defaults to :class:`False`
        :param int close_timeout: Seconds after the websocket will timeout after the handshake
                                  didn't complete successfully. Defaults to :class:`40`

        :param event_loop: Event Loop that will be used for running the client and it's methods
                           Uses `asyncio.get_event_loop()` to fetch the current event_loop. Creates a new one
                           if no existing is found!
        :type event_loop: :class:`asyncio.AbstractEventLoop`

        :raises InvalidClientType: If a faulty Client Type was passed!
        :raises InvalidToken: If an empty, faulty or None Type Token was passed!
        :raises ImportError: If an required module is missing and not installed!

==========
UserClient
==========

    .. py:class:: UserClient(token, *, event_loop, kwargs**)

        Bot Client Class used for bot accounts that are registered on Hiven.

        .. note::
            The Bot Client is currently not entirely optimised for all API Features!
            Please report errors or missing features that need to be implemented!

        :param str token: Token for the interaction with Hiven.
        :param bool restart: If set to True will automatically restart the websocket once if
                             an error occurred while running. Defaults to :class:`False`
        :param str client_type:  Automatically set if UserClient or BotClient is used.
                                 Defaults to `bot`
        :param event_handler: Event Handler Class that will be used to trigger events!
                              Creates a new EventHandler on Default
        :type event_handler: :class:`openhivenpy.events.EventHandler`
        :param int heartbeat: Heartbeat interval for sending a lifesignal to Hiven.
                              Defaults to :class:`30000` (in milliseconds)
        :param bool log_ws_output: If set to :class:`True`, the websocket will log automatically
                                   all incoming json data. Can provide even more insight to the
                                   Hiven Swarm. Defaults to :class:`False`
        :param int close_timeout: Seconds after the websocket will timeout after the handshake
                                  didn't complete successfully. Defaults to :class:`40`

        :param event_loop: Event Loop that will be used for running the client and it's methods
                           Uses `asyncio.get_event_loop()` to fetch the current event_loop. Creates a new one
                           if no existing is found!
        :type event_loop: :class:`asyncio.AbstractEventLoop`

        :raises InvalidClientType: If a faulty Client Type was passed!
        :raises InvalidToken: If an empty, faulty or None Type Token was passed!
        :raises ImportError: If an required module is missing and not installed!

        .. py:function:: fetch_current_friend_requests()

            Fetches all open friend requests on Hiven

            :async:
            :return: A dict with all incoming and outgoing friend requests
            :rtype: dict

        .. py:function:: block_user(user_id, user)

            Blocks the user if the user exists.

            Only needs one parameter to work! Will default to user_id if both parameters are passed!

            :async:
            :param user_id: User Object. Defaults to `None`
            :type user_id: int
            :param user: User Object. Defaults to `None`
            :type user: `openhivenpy.types.User <User>`_
            :return: Returns `True` if the request succeeded else `False`
            :rtype: dict or None

        .. py:function:: unblock_user(user_id, user)

            Unblocks the user if the user exists and the user is blocked!

            Only needs one parameter to work! Will default to user_id if both parameters are passed!

            :async:
            :param user_id: User Object. Defaults to `None`
            :type user_id: int
            :param user: User Object. Defaults to `None`
            :type user: `openhivenpy.types.User <User>`_
            :return: Returns `True` if the request succeeded else `False`
            :rtype: dict or None

        .. py:function:: send_friend_request(user_id, user)

            Sends the user a friend request.

            Only needs one parameter to work! Will default to user_id if both parameters are passed!

            :async:
            :param user_id: User Object. Defaults to `None`
            :type user_id: int
            :param user: User Object. Defaults to `None`
            :type user: `openhivenpy.types.User <User>`_
            :return: Returns `True` if the request succeeded else `False`
            :rtype: bool

        .. py:function:: cancel_friend_request(user_id, user)

            Cancels a friend requests if it exists.

            Only needs one parameter to work! Will default to user_id if both parameters are passed!

            :async:
            :param user_id: User Object. Defaults to `None`
            :type user_id: int
            :param user: User Object. Defaults to `None`
            :type user: `openhivenpy.types.User <User>`_
            :return: Returns `True` if the request succeeded else `False`
            :rtype: bool
