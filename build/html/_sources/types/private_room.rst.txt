************
Private Room
************

.. note:: This is not to be confused with PrivateGroupRoom! PrivateGroupRoom is for private non-group rooms, whilst PrivateRoom is private non-group rooms. 

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

.. py:function:: send(content, delay = 0)

    Sends a message in the room

    :async:
    :param content: The message's content
    :type content: :class:`str`
    :param attatchment: The message's attatchment
    :type attatchment: :class:`binary`
    :param delay: Delay until execution
    :type delay: :class:`float`
    :returns: :class:`Message`
    :rtype: :class:`Message`