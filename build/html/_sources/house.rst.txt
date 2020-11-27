*****
House
*****

.. attribute :: id

    The ID relating to the house.

.. attribute :: name

    The house's name

.. attribute  :: banner

    The house's banner.

.. attribute :: icon

    The house's icon. Returns Hiven's cdn link

.. attribute :: owner_id

    Returns the house owner's ID

.. attribute :: roles

    Returns the house's roles

.. attribute :: members

    Returns the house's members

.. attribute :: users

    Alias for :attr:`members`

.. function :: get_member(member_id)

    Grabs a member via id. Returns :class:`Member` if successful.

    :param member_id: The ID of the member.
    :type member_id: :class:`int`
    :returns: :class:`Member`

.. function :: create_room(name)

    Creates a room in the current house. Requires permissions to execute. Returns the created :class:`Room`.

    :param name: The house name
    :type name: :class:`str`
    :returns: :class:`Room`

.. function :: leave()

    Leaves the current house. Returns `True` if successful.

    :returns: :class:`bool`

.. function :: edit(kwargs)

    Edits the current house. Requires the user to have permissions. Returns True if successful.

    :param name: House name
    :type name: :class:`str`
    :param icon: House icon
    :type icon: :class:`base64`
    :returns: :class:`bool`

.. function :: create_invite()

    Creates an invite for the current house. Returns the invite if successful.

    :returns: :class:`str`