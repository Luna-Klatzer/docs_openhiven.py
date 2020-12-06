****
Room
****

.. attribute :: id

    Returns the room ID

.. attribute :: name

    Returns the rooms name

.. attribute :: house

    Returns the house the room belongs in

.. attribute :: position

    Returns the position of the room in the category

.. attribute :: emoji

    Returns the room's emoji

.. attribute :: description

    Returns the room's description

.. function :: send(kwargs)

    Sends a message in the Room. Returns the message if successful.

    :param content: The content of the message
    :type content: :class:`string`
    :param delay: The delay before sending the message. Defaults to 0.
    :type delay: :class:`float`
    :param attatchment: The attatchment to send with the message. Defaults to None
    :type attatchment: :class:`file`
    :returns: :class:`Message`

.. function :: edit(kwargs)

    Edits the Room. The client needs permissions to do this. Returns True if successful.

    :param name: The room name
    :type name: :class:`string`
    :param emoji: The room's emoji
    :type emoji: :class:`string`
    :param description: The room's description
    :type description: :class:`string`