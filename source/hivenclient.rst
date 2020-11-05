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

      **Parameter:**
         :param str token: Token for the interaction with Hiven. 

                              Raises Exception InvalidToken if None, empty String or length not 128

         :param int heartbeat: Hearbeat interval for sending messages to the Hiven Websocket
         :param bool print_output: If set to True the raw messages that were received on the Websocket will be printed out! Defaults to False
         :param bool debug_mode: If set to True the following will be printed out:
                                 * Data is sent to Hiven
                                 * Data is received from Hiven
                                 * An event was triggered
                                 * A command was used
                                 Defaults to False

         :param str client_type: Type of the HivenClient. Can only be either "user", "bot" or None.
         
         .. note:: Will be automatically set if :ref:`Bot Client<BotClient>` or :ref:`User Client<UserClient>` is used!
                  If the HivenClient: :ref:`HivenClient` is directly used as an object, it is recommended to set it to None!

      .. py:method:: deactivate_print_output() -> None


=========
BotClient
=========


==========
UserClient
==========
