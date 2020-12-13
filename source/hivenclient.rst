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

   .. py:class:: HivenClient(args*, kwargs**)

      Main Class used to interact with the Websocket and the Hiven API.
      Inherited by :ref:`BotClient<BotClient>` and :ref:`UserClient<UserClient>`

      :param str token: Token for the interaction with Hiven. 
      :param bool restart: If set to True will automatically restart the websocket once if
                     an error occurred while running. Defaults to :class:`False`
      :param str client_type:  Automatically set if UserClient or BotClient is used.
                           Defaults to `BotClient` and will be automatically set if using BotClient or UserClient
      :param event_handler: Event Handler Class that will be used to trigger events!
                           Creates a new EventHandler on Default
      :type event_handler: :class:`openhivenpy.events.EventHandler`
      :param int heartbeat: Heartbeat interval for sending a lifesignal to Hiven.
                           Defaults to :class:`30000` (in milliseconds)
      :param bool log_ws_output: If set to :class:`True`, the websocket will log automatically
                                 all incoming json data. Can provide even more insight to the
                                 Hiven Swarm. Defaults to :class:`False`
      :param int ping_timout: Seconds after the websocket will timeout after no successful pong response.
                              More information on the websockets documentation. Defaults to :class:`100`
      :param int close_timeout: Seconds after the websocket will timeout after the handshake
                                 didn't complete successfully. Defaults to :class:`20`
      :param int ping_interval: Interval for sending pings to the server. Defaults to :class:`None` 

         .. Note::
            Changing the Ping Interval can cause the WebSocket connection to break, since currently
            when pinging Hiven, no response will be received and so the Connection would timeout itself!

      :param event_loop: Event Loop that will be used for running the client and it's methods
      :type event_loop: :class:`asyncio.AbstractEventLoop`

      :raises InvalidClientType: If a faulty Client Type was passed!
      :raises InvalidToken: If an empty, faulty or None Type Token was passed!
      :raises ImportError: If an required module is missing and not installed!
   
      .. py:function:: run()

         Starts the HivenClient and the Websocket Connection to Hiven

         Wraps the :ref:`connect()<connect>` coroutine

      .. _connect:

      .. py:function:: connect()

         This function is a coroutine

         Starts the HivenClient and the Websocket Connection to Hiven

      .. py:function:: stop()

         This function is a coroutine

         Stops the current session if an active connection exists

      .. attribute:: token

         Token used to connect to Hiven

         :type: :class:`str`

      .. attribute:: open

         If :class: `True` connection is open

         :type: :class:`bool`

      .. attribute:: closed

         Counter attribute to open

         If :class: `True` connection is closed

         :type: :class:`bool`

      .. attribute:: ready

         If :class:`True` the client has received all data from Hiven and is ready for use

         :type: :class:`bool`

      .. attribute:: initialized

         If :class:`True` the Websocket and HTTPClient are connected and running

         .. Note::
            The attribute:class:`initialized` is not the same as :attr:`ready`!
            
            It only represents an active connection to Hiven and should not be used to trigger interaction with Hiven!

         :type: :class:`bool`

      .. attribute:: http_client

         HTTP-Client used for requests to Hiven. 
         
         Can be used to execute manual requests. See `HTTPClient <https://openhivenpy.readthedocs.io/en/stable/advanced_usage/http_client.html>`_ for more info 

         :type: :class:`openhivenpy.gateway.HTTPClient`

      .. attribute:: client_type

         Client Type

         Can be either :class:`HivenClient.BotClient`, :class:`bot`, :class:`HivenClient.UserClient` or :class:`user`

         :type: :class:`str`

      .. attribute:: heartbeat

         Heartbeat of the Websocket

         :type: :class:`int`

      .. attribute:: connection_status

         Connection Status of the Client

         Can be either :class:`OPENING`, :class:`OPEN`, :class:`CLOSING` or :class:`CLOSED`

         :type: :class:`str`

      .. attribute:: websocket

         Websocket object that is used connecting to Hiven

         .. Note::
            Currently not working and will throw an error!
            Will be fixed in :math:`0.1.1`


         :type: :class:`openhivenpy.gateway.Websocket`

      .. attribute:: startup_time

         Time that it took the client to started

         :type: :class:`int`

=========
BotClient
=========

==========
UserClient
==========
