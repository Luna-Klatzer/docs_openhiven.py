************
Private Room
************

.. py:class:: PrivateRoom

    Represents a private message room with another user or bot

    .. note::

        This is not to be confused with PrivateGroupRoom!
        PrivateGroupRoom is for private non-group rooms, whilst PrivateRoom is private non-group rooms.

    .. attribute:: user

        The user in the room

    .. attribute:: recipient

        Aliases of :attr:`user`

    .. attribute:: id

        The ID of the room

    .. attribute:: last_message_id

        The last message's ID

    .. attribute:: name

        The name of the room

    .. py:function:: send(content, delay)

        This function is a coroutine!

        Sends a message in the room

        :param content: The message's content
        :type content: str
        :param attatchment: The message's attachment
        :type attatchment: :class:`binary`
        :param delay: Delay until execution
        :type delay: float
        :return: The `Message` object if successful else `None`
        :rtype: :class:`Message`

******************
Private Group Room
******************

.. py:class:: PrivateGroupRoom

    Represents a private group room with other users

    .. attribute:: user

        The users in the Group Room

    .. attribute:: recipient

        Aliases of :attr:`user`

    .. attribute:: id

        The ID of the Group

    .. attribute:: last_message_id

        The last message's ID

    .. attribute:: name

        The name of the Group

    .. py:function:: send(content, delay)

        This function is a coroutine!

        Sends a message in the room

        :param content: The message's content
        :type content: str
        :param delay: Delay until execution. Defaults to 0
        :type delay: float
        :return: The `Message` object if successful else `None`
        :rtype: :class:`Message`