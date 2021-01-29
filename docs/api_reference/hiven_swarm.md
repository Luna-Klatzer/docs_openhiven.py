# Hiven Swarm

---

!!! Warning

    **This documentation page is not finished yet! Information can be outdated or entirely not available!**


## Swarm Events

### `INIT_STATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "user": {
        "username": str,
        "user_flags": str,
        "name": str,
        "id": str,
        "icon": str,
        "header": str,
        "presence": str
    },
    "settings": {
        "user_id": str,
        "theme": None,
        "room_overrides": {
            // room preferences mapped to their id
            "id": { 
                "notification_preference": int 
            }
        },
        "onboarded": unknown,
        "enable_desktop_notifications": unknown
    },
    "relationships": {
        "id": {
            "user_id": str,
            "user": {
                "username": str,
                "user_flags": str,
                "name": str,
                "id": str,
                "icon": str,
                "header": str,
                "presence": str
            },
            "type": int,
            "last_updated_at": str
        },
    },
    "read_state": {
        "id": {
          "message_id": str,
          "mention_count": int
        },
    },
    "private_rooms": [{
        "default_permission_override": None
        "description": str,
        "emoji": object,
        "house_id": None,
        "id": str,
        "last_message_id": str,
        "name": str,
        "owner_id": str,
        "permission_overrides": None
        "position": None
        "recipients": [{  
            // User Object
            "username": str,
            "user_flags": str,
            "name": str,
            "id": str,
            "icon": str,
            "header": str,
            "presence": str
        } ... ],
        "type": int
    } ... ],
    "presences": {
        "id": {
          "username": str,
          "user_flags": str,
          "name": str,
          "id": str,
          "icon": str,
          "header": str,
          "presence": str
        }
    },
    "house_memberships": [{
        "id": {
            "user_id": str,
            "user": {
                // User Object
                "username": str,
                "user_flags": str,
                "name": str,
                "id": str,
                "icon": str,
                "header": str,
                "presence": str
            },
            "roles": [],
            "last_permission_update": str,
            "joined_at": str,
            "house_id": str,
        }
    } ... ],
    "house_ids": [
        // list of house_ids
        "house_id",
        ...
    ]
  }
}
```

### `HOUSE_JOIN`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_house_join()`]()

```json
"op": 0,
"d": {
    "rooms": [{
        // Room Object
        "type": int,
        "recipients": None
        "position": int,
        "permission_overrides": bits,
        "owner_id": str,
        "name": str,
        "last_message_id": str,
        "id": str,
        "house_id": str,
        "emoji": object,
        "description": str,
        "default_permission_override": int
    }, ...],
    "roles": [{
        // Role Object
        "position": int,
        "name": str,
        "level": int,
        "id": str,
        "deny": bits,
        "color": str,
        "allow": bits
    }],
    "owner_id": str,
    "name": str,
    "members": [{
        // Member Object
        "user_id": str,
        "user": {
            // User Object
            "username": str,
            "user_flags": str,
            "name": str,
            "id": str,
            "icon": str,
            "header": str,
            "presence": str
        },
        "roles": [
            "position": int,
            "name": str,
            "level": int,
            "id": str,
            "deny": bits,
            "color": str,
            "allow": bits
        ],
        "last_permission_update": str,
        "joined_at": str,
        "house_id": str
    }],
    "id": str,
    "icon": str,
    "entities": [{
        // Entity Object
        "type": int,
        "resource_pointers": [{
            // Resource Pointer
            "resource_type": str,
            "resource_id": str
        } ... ],
        "position": int,
        "name": str,
        "id": str
    } ... ],
    "default_permissions": int,
    "banner": str
}
```

### `HOUSE_LEAVE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
  "id": str,
  "house_id": str
}
```

### `BATCH_HOUSE_MEMBER_UPDATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "house_id": str,
    "batch_type": [],
    "batch_size": int,
    "data": {
        // Collection of Members that are mapped to their id
        "id": {
            // Member Object
            "user_id": str,
            "user": {
                // User Object
                "username": str,
                "user_flags": str,
                "name": str,
                "id": str,
                "icon": str,
                "header": str,
                "presence": str
            },
            "roles": [{
                // Role Object
                "position": int,
                "name": str,
                "level": int,
                "id": str,
                "deny": bits,
                "color": str,
                "allow": bits
            } ... ],
            "last_permission_update": str,
            "joined_at": str,
            "house_id": str
        }
    }
}
```

### `RELATIONSHIP_UPDATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "user": {
        // User Object
        "website": str,
        "username": str,
        "user_flags": int,
        "name": str,
        "location": str,
        "id": str,
        "icon": str,
        "bio": str
    },
    "type": int,
    "recipient_id": str,
    "id": str
}
```

### `MESSAGE_CREATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "timestamp": int,
    "room_id": str,
    "mentions": [{
        // Mention object aka. user object
        "username": str,
        "user_flags": str,
        "name": str,
        "id": str,
        "icon": str,
        "header": str,
        "presence": str,
        "bot": bool
    } ... ],
    "member": {
        // Member Object
        "user_id": str,
        "user": {
            // User Object
            "username": str,
            "user_flags": str,
            "name": str,
            "id": str,
            "icon": str,
            "header": str,
            "presence": str
        },
        "roles": [{
            // Role Object
            "position": int,
            "name": str,
            "level": int,
            "id": str,
            "deny": bits,
            "color": str,
            "allow": bits
        } ... ],
        "last_permission_update": str,
        "joined_at": str,
        "house_id": str
    },
    "id": str,
    "house_id": str,
    "exploding_age": int,
    "exploding": bool,
    "device_id": str,
    "content": str,
    "bucket": int,
    "author_id": str,
    "author": {
        // User Object
        "username": str,
        "user_flags": str,
        "name": str,
        "id": str,
        "icon": str,
        "header": str,
        "presence": str
    }
    "attachment": {
        // Attachment Object
        "media_url": str,
        "filename": str,
        "dimensions": {
            "width": int,
            "type": str,
            "height": int
        }
    }
}
```

### `MESSAGE_DELETE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "room_id": str,
    "message_id": str,
    "house_id": str
}
```

### `MESSAGE_UPDATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "type": int,
    "timestamp": str,
    "room_id": str,
    "metadata": unknown,
    "mentions": [{
        // Mention object aka. user object
        "username": str,
        "user_flags": str,
        "name": str,
        "id": str,
        "icon": str,
        "header": str,
        "presence": str
    }, ...],
    "id": str,
    "house_id": str,
    "exploding_age": int,
    "exploding": bool,
    "embed": {
        // Embed Object
    },
    "edited_at": str,
    "device_id": str,
    "content": str,
    "bucket": int,
    "author_id": str,
    "attachment": {
        // Attachment Object
        "media_url": str,
        "filename": str,
        "dimensions": {
            "width": int,
            "type": str,
            "height": int
        }
    }
}
```

### `PRESENCE_UPDATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    // User Object
    "username": str,
    "user_flags": str,
    "name": str,
    "id": str,
    "icon": str,
    "header": str,
    "presence": str
}
```

### `ROOM_CREATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "house_id": str,
    "id": str,
    "name": str,
    "position": int,
    "type": int
}
```
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
### `ROOM_UPDATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
```

### `ROOM_DELETE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
```

### `HOUSE_MEMBER_JOIN`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "house_id": str,
    "joined_at": timestamp,
    "roles": [{
        // Role Object
        "position": int,
        "name": str,
        "level": int,
        "id": str,
        "deny": bits,
        "color": str,
        "allow": bits 
    } ... ],
    "length": int
    "user": {
        "id": str,
        "name": str,
        "user_flags": str,
        "username": str,
    }
}
```

### `HOUSE_MEMBER_EXIT`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "id": str,
    "house_id": str
}
```

### `HOUSE_MEMBER_ENTER`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "user_id": str,
    "user": {
        "username": str,
        "user_flags": str,
        "name": str,
        "id": str,
        "icon": str,
        "bot": bool,
    },
    "roles": [{
        // Role Object
        "position": int,
        "name": str,
        "level": int,
        "id": str,
        "deny": bits,
        "color": str,
        "allow": bits 
    } ... ],
    "presence": str,
    "last_permission_update": null,
    "joined_at": str,
    "id": str,
    "house_id": str
}
```

### `HOUSE_MEMBER_UPDATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "user_id": str,
    "user": {
        // User Object
        "website": str,
        "username": str,
        "user_flags": int,
        "name": str,
        "location": str,
        "id": str,
        "icon": str,
        "header": str,
        "email_verified": bool,
        "bot": bool,
        "bio": str
    },
    "roles": [{
        // Role Object
        "position": int,
        "name": str,
        "level": int,
        "id": str,
        "deny": bits,
        "color": str,
        "allow": bits 
    } ... ],
    "presence": str,
    "last_permission_update": unknown,
    "joined_at": str,
    "id": str,
    "house_id": str
}
```

### `HOUSE_MEMBERS_CHUNK`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
    "members": [{
        "id": {
            "user_id": str,
            "user": {
            "username": str,
            "user_flags": str,
            "name": str,
            "id": strstr
            "icon": str,
            "header": str,
            "presence": str
        },
        "roles": [{
            // Role Object
            "position": int,
            "name": str,
            "level": int,
            "id": str,
            "deny": bits,
            "color": str,
            "allow": bits 
        } ... ],
        "last_permission_update": str,
        "joined_at": str,
        "house_id": str
        }
    } ... ],
    "house_id": str
}
```
        
### `TYPING_START`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0
"d": {
  "timestamp": int,
  "room_id": str,
  "house_id": str,
  "author_id": str
}
```

### `HOUSE_ENTITY_UPDATE`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0
"d": {
    "house_id": str,
    "entities": [{
        "type": int,
        "resource_pointers": [{
            // Resource Pointer
            "resource_type": str,
            "resource_id": str
        } ... ],
        "position": int,
        "name": str,
        "id": str
    } ... ]
}
```

### `HOUSE_DOWN`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_init()`]()

Expected json-data: 
```json
"op": 0,
"d": {
  "unavailable": bool,
  "house_id": str
}
```
