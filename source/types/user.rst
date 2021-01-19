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
