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