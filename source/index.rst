.. OpenHiven.py documentation master file, created by
   sphinx-quickstart on Mon Nov  2 19:15:19 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. role:: raw-html(raw)
    :format: html

.. _Start:

==========================
OpenHiven.py documentation
==========================

The Unofficial Python API wrapper for Hiven. For sourcode go to the Github Repository

.. _Hiven: https://hiven.io/

.. toctree::
   :caption: Table of Contents
   :name: openhiven.py
   HivenClient
   Websocket
   BotClient
   UserClient

HivenClient
===========

   .. py:class:: openhivenpy.Client.HivenClient(args*, kwargs**)

         Main Class used to interact with the Websocket and the Hiven API.
         Inherited by BotClient: :ref:`Bot Client` and UserClient: :ref:`User Client`

         **Parameter:**

            :param str token: Token for the interaction with Hiven. 

                              Raises Exception InvalidToken if None, empty String or length not 128
            :param str client_type: Type of the HivenClient. Can only be either "user", "bot" or None.
               .. note:: 
               Will be automatically set if :ref:`Bot Client<Bot Client>` or :ref:`User Client<User Client>` is used!

               If the HivenClient: :ref:`HivenClient` is directly used as an object, it is recommended to set it to None!
            :param int heartbeat: Hearbeat interval for sending messages to the Hiven Websocket
            :param bool print_output: If set to True the raw messages that were received on the Websocket will be printed out! Defaults to False
            :param bool debug_mode: If set to True the following will be printed out:
                                    * Data is sent to Hiven
                                    * Data is received from Hiven
                                    * An event was triggered
                                    * A command was used
                                    Defaults to False

         .. py:method:: deactivate_print_output() -> None


Websocket
=========

   .. py:class:: openhivenpy.Websocket.**Websocket**(args*, kwargs**)

Bot Client
==========


User Client
===========
