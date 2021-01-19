****
Room
****

.. py:class:: Room

    Represents a Hiven Room in a House

    .. attribute:: id

        Returns the room ID

    .. attribute:: name

        Returns the rooms name

    .. attribute:: house

        Returns the house the room belongs in

    .. attribute:: position

        Returns the position of the room in the category

    .. attribute:: emoji

        Returns the room's emoji

    .. attribute:: description

        Returns the room's description

    .. function:: send(kwargs)

        Sends a message in the Room. Returns the message if successful.

        :async:
        :param content: The message's content
        :type content: str
        :param delay: Delay until execution. Defaults to 0
        :type delay: float
        :return: The message object if successful else `None`
        :rtype: :class:`Message`

    .. function:: edit(**kwargs)

        Edits the Room. The client needs permissions to do this.

        :async:
        :param name: The room name
        :type name: str
        :param emoji: The room's emoji
        :type emoji: str
        :param description: The room's description
        :type description: str
        :return: `True` if successful else `False`
        :rtype: bool