*****************
Class HivenClient
*****************

.. role:: raw-html(raw)
    :format: html

.. _Start:

===========
HivenClient
===========

   .. py:class:: openhivenpy.Client.HivenClient(args*, kwargs**)

      Main Class used to interact with the Websocket and the Hiven API.
      Inherited by :ref:`Bot Client<BotClient>` and :ref:`User Client<UserClient>`

      :param token: Token for the interaction with Hiven. 
      :type token: :class:`string`
      :param heartbeat: Hearbeat interval for sending messages to the Hiven Websocket
      :type token: :class:`int`
      :param str client_type: Type of the HivenClient. Can only be either "user", "bot" or None.
         
         .. note:: 
            Will be automatically set if :ref:`Bot Client<BotClient>` or :ref:`User Client<UserClient>` is used!
            If the HivenClient: :ref:`HivenClient` is directly used as an object, it is recommended to set it to None!

=========
BotClient
=========


==========
UserClient
==========
