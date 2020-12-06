*******
Message
*******

.. attribute :: id

    Grabs the ID of the message.

.. attribute :: author

    Grabs the author of the message.

.. attribute :: created_at

    Grabs the time the message was sent.

.. attribute :: edited_at

    Grabs the time the message was edited. Will return None if it hasn't been edited.

.. attribute :: room

    Grabs the :class:`Room` the message belongs to

.. attribute :: house

    Grabs the :class:`House` the message belongs to. May return None in a :class:`Private Room`

.. attribute :: attatchment

    Grabs the :class:`Attatchment` of the message. May return None.

.. attribute :: content

    Grabs the message's content.

.. attribute :: mentions

    Grabs a list of mentions in the message. May return None.

.. attribute :: embed

    Grabs the embed in the message.

.. function :: mark_message_as_read(delay = 0)

    Marks the message as read. Bot clients do not need to use this. 

    :param delay: Delay until execution
    :type delay: :class:`float`
    :returns: :class:`bool`

.. function :: delete(delay = 0)

    Deletes the message. Raises :exception:`Forbidden` if not allowed.

    :param delay: Delay until execution
    :type delay: :class:`float`
    :returns: :class:`DeletedMessage`

.. function :: edit(content)

    Edits the message. Returns True if successful.

    :param content: The message's content.
    :type content: :class:`string`
    :returns: :class:`bool`