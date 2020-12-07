******************
Private Group Room
******************

.. note:: This is not to be confused with PrivateRoom! PrivateRoom is for private non-group rooms, whilst PrivateGroupRoom is private group rooms. 

.. attribute :: user

    The users in the Group Room

.. attribute :: recipient

    Aliases of :attr:`user`

.. attribute :: id

    The ID of the Group
    
.. attribute :: last_message_id

    The last message's ID

.. attribute :: name

    The name of the Group

.. function :: send(content,delay = 0)

    Sends a message in the group

    :param content: The message's content
    :type content: :class:`str`
    :param attatchment: The message's attatchment
    :type attatchment: :class:`binary`
    :param delay: Delay until execution
    :type delay: :class:`float`
    :returns: :class:`Message`