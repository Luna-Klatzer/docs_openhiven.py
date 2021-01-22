***********
Data Models
***********

To represent data more intractable and more user-friendly, openhiven.py uses a data model system which represents
data in object form which can be used to interact with the Hiven API directly and access data easily.

.. note::

    Data-models are still in development and therefore can partly have not entirely working API methods.
    If issues are found please report them on the github issues page. (More infos on Bug-Reporting on the according
    `docs-page <https://openhivenpy.readthedocs.io/en/stable/intro/bug_reporting.html>`_)

***********
Attachment
***********

.. py:class:: Attachment

    Represents a Hiven Attachment

    .. attribute:: filename

        Returns the file's filename.

    .. attribute:: media_url

        Returns the file's URL in Hiven's CDN.

    .. attribute:: raw

        Returns the raw data sent from Hiven. Useful for image sizes

********
Category
********

.. py:class:: Category

    Represents a Hiven Entity

*******
Context
*******

.. py:class:: Context

    Represents a Command Context for a triggered command in the CommandListener

    .. note::

        Currently not accessible since no CommandListener was implemented yet

*****
Embed
*****

.. py:class:: Embed

    Represents a Command Context for a triggered command in the CommandListener

    .. note::

        Currently not accessible since no CommandListener was implemented yet

    .. attribute:: url

        Returns the URL the embed is linked to.

    .. attribute:: type

        Returns the type (in :class:`int`) for the embed.

    .. attribute:: title

        Returns the title for the embed.

    .. attribute:: image

        Returns the image for the embed.

    .. attribute:: description

        Returns the description for the embed.

****
Feed
****

.. py:class:: Feed

    Represents a Client Feeds of the User

*****
House
*****

.. py:class:: House

    Represents a Hiven House Object

    .. attribute:: id

        Returns the ID relating to the house.

    .. attribute:: name

        Returns the house's name

    .. attribute:: banner

        Returns the house's banner.

    .. attribute:: icon

        Returns the house's icon in the correct link format

    .. attribute:: owner_id

        Returns the house owner's ID

    .. attribute:: roles

        Returns the house's roles

    .. attribute:: members

        Returns the house's members

    .. attribute:: users

        Alias for :attr:`members`

    .. function:: get_member(member_id)

        Fetches a member based on their id.

        :param member_id: The ID of the member.
        :type member_id: int
        :return: The user if found else None
        :rtype: :class:`Member`

    .. function:: create_room(name)
        :async:

        Creates a room in the current house.

        Requires permissions to execute. Will automatically fail if not sufficient!

        :param name: The house name
        :type name: str
        :return: The generated room if successful else None
        :rtype: :class:`Room`

    .. function:: leave()
        :async:

        Leaves the current house.

        :return: True if successful else False
        :rtype: bool

    .. function:: edit(**kwargs)
        :async:

        Edits the current house. Requires the user to have permissions.

        :param name: House name
        :type name: str
        :param icon: House icon
        :type icon: :class:`base64`
        :return: True if successful else False
        :rtype: bool

    .. function:: create_invite()
        :async:

        Creates an invite for the current house.

        :return: The new generated invite link of the House if the request was successful else None
        :rtype: str or None

******
Invite
******

.. py:class:: Invite

    Represents a Hiven Invite to a House

    .. attribute:: code

        Returns the invite code itself

    .. attribute:: url

        Returns the :attr:`code` in correct usage format

    .. attribute:: house

        Returns the house of the invite

    .. attribute:: max_age

        Returns the max age of the invite

    .. attribute:: max_uses

        Returns the maximum usage of the invite

    .. attribute:: house_members

        Returns the amount of members of the house the invite is linked to

******
Member
******

.. py:class:: Member

    Represents a Hiven Member of a House

*******
Mention
*******

.. py:class:: Mention

    Represents a Hiven Mention in a message

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
        :async:

        Marks the message as read. Bot clients do not need to use this.

        :param delay: Delay until execution
        :type delay: float
        :return: `True` if successful else `False`
        :rtype: bool

    .. function:: delete(delay = 0)
        :async:

        Deletes the message. Raises :class:`Forbidden` if not allowed.

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

********
Presence
********

.. py:class:: Presence

    Represents a user's current visible presence

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

        Aliases for :attr:`user`

    .. attribute:: id

        The ID of the room

    .. attribute:: last_message_id

        The last message's ID

    .. attribute:: name

        The name of the room

    .. function:: send(content, delay)
        :async:

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

    .. attribute:: recipients

        Recipients in the :class:`PrivateGroupRoom`

    .. attribute:: id

        The ID of the Group

    .. attribute:: last_message_id

        The last message's ID

    .. attribute:: name

        The name of the Group

    .. function:: send(content, delay)
        :async:

        Sends a message in the room

        :param content: The message's content
        :type content: str
        :param delay: Delay until execution. Defaults to 0
        :type delay: float
        :return: The `Message` object if successful else `None`
        :rtype: :class:`Message`

************
Relationship
************

.. py:class:: Relationship

    Represents a Relationship between a user and the Client

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
        :async:

        Sends a message in the Room. Returns the message if successful.

        :param content: The message's content
        :type content: str
        :param delay: Delay until execution. Defaults to 0
        :type delay: float
        :return: The message object if successful else `None`
        :rtype: :class:`Message`

    .. function:: edit(**kwargs)
        :async:

        Edits the Room. The client needs permissions to do this.

        :param name: The room name
        :type name: str
        :param emoji: The room's emoji
        :type emoji: str
        :param description: The room's description
        :type description: str
        :return: `True` if successful else `False`
        :rtype: bool

******
Typing
******

.. py:class:: Typing

    Represents a user typing

    .. note::

        Will likely be removed in the future!

****
User
****

.. py:class:: User

    Represents a global User on Hiven

    .. attribute:: id

        Returns the user's ID

    .. attribute:: username

        Returns the user's username. Not to be confused with :attr:`name`.

    .. attribute:: name

        Returns the user's name.

    .. attribute:: icon

        Returns the user's icon.

    .. attribute:: header

        Returns the user's header. This is called a banner in Hiven's UI.

    .. attribute:: bot

        Returns `True` if the user is a bot

    .. attribute:: location

        Returns the user's location. Returns `None` if they don't have one set.

    .. attribute:: website

        Returns the user's website. Returns `None` if they don't have one set.

    .. attribute:: presence

        Returns the user's :class:`Presence`

    .. attribute:: joined_at

        Returns the date and time the user joined Hiven.

