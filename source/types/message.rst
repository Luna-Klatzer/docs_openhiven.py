*******
Message
*******

.. py:class:: Message

    .. attribute:: id
    
        Returns the ID of the message.
    
    .. attribute:: author
    
        Returns the author of the message.
    
    .. attribute:: created_at
    
        Returns the time the message was sent.
    
    .. attribute:: edited_at
    
        Returns the time the message was edited. Will return None if it hasn't been edited.
    
    .. attribute:: room
    
        Returns the :class:`Room` the message belongs to
    
    .. attribute:: house
    
        Returns the :class:`House` the message belongs to. May return None in a :class:`Private Room`
    
    .. attribute:: attachment
    
        Returns the :class:`Attachment` of the message. May return None.
    
    .. attribute:: content
    
        Returns the message's content.
    
    .. attribute:: mentions
    
        Returns the list of mentions in the message. May return None.
    
    .. attribute:: embed
    
        Returns the embed in the message.
    
    .. function:: mark_message_as_read(delay)
    
        Marks the message as read. Bot clients do not need to use this. 

        :async:
        :param delay: Delay until execution
        :type delay: float
        :return: `True` if successful else `False`
        :rtype: bool
    
    .. function:: delete(delay = 0)
    
        Deletes the message. Raises :class:`Forbidden` if not allowed.

        :async:
        :param delay: Delay until execution
        :type delay: float
        :return: The `DeletedMessage` object if successful else `False`
        :rtype: :class:`DeletedMessage`
    
    .. function:: edit(content)
    
        Edits the message. Returns True if successful.
    
        :param content: The message's content.
        :type content: str
        :rtype: bool

***************
Deleted Message
***************


.. py:class:: DeletedMessage

    Represents a deleted Message in a room

    .. attribute:: house_id

        Returns the house id of the message

    .. attribute:: message_id

        Returns the message id of the message

    .. attribute:: room_id

        Returns the room id of the message
