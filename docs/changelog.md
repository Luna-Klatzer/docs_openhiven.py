# Changelog

---

## v0.1.2

[PyPi Release](https://pypi.org/project/openhivenpy/0.1.2/)

Websocket and HTTP Cleanup Update for bug-fixes, handling-improvements and greater speed and efficiency

!!! tip "Changelog"

    * Rewrite of core Websocket Event Handling:
       * Moved handler methods from `response_handler` to the websocket object itself (Will be changed in the Websocket Rewrite
         and EventHandling Update)
    * Added traceback to in-code exceptions for easier debugging and testing
    * Renamed `EventHandler` event-function names and changed name prefix to `dispatch_{event_name}`
    * Rewrote restart handler and moved the instantiation of the loop from `Connection.connect()` to `HivenClient.run()` and `HivenClient.connect()` to not be dependent on the connection object itself. This will avoid that the restart handler is also affected when the connection fails due to an exception.
    * Fixed `Client.edit(**kwargs)` bug causing issues with data being passed as json without correct formatting.
      Caused by `HTTP.patch()` faulty param passing to `HTTP.raw_request()`
    * Added proper docs to the HTTP Class, and it's methods
    * Added `json` and `header` with default `None` as parameters to the HTTP method requests. If they are not overwritten by a passed parameter:
        * param json: Will not get passed to the requests to allow a `data` field of any type
        * param headers: Will be overwritten by the default headers, and the passed as an argument to the request
    * Added `on_house_delete` and `on_house_member_leave` as events and added correct handling
    * Fixed `room_create` as event and added group room creation
    * Added better traceback for exceptions, including event_listener methods to avoid that asyncio exceptions are thrown and added `log_traceback(level='error', msg='Traceback: ', suffix=None)` as function to utils
    * Fixed `HOUSE_MEMBER_EXIT` bug causing members to be removed from houses instead of being set offline
    * Renamed `on_house_member_exit` to `on_house_member_offline` and `on_house_member_enter` to `on_house_member_online`
    * Fixed `fetch_invite()` and `Invite` Object Creation bug
    * Added until now missing entity object to the event `on_house_entity_update`
    * Renamed object `Category` to `Entity` to be equivalent to the Hiven API
    * Added `create_private_group_room` as method in the class `HivenClient`
    * Rewrote `create_private_room` in `HivenClient` to take only the `user` parameter instead of `user_id` and `user`
    * Fixed attribute `joined_at` in the class `Member`
    * Added `username` option for `Client.edit(**kwargs)`
    * Removed `joined_at` from `User`
    * Fixed cache lists reference error caused by prior commits (houses, rooms, users etc.)
    * Removed `ping` from the HivenClient (Will be added back later but with better implementation)