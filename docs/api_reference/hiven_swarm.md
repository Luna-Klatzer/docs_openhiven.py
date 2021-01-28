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
    "private_rooms": [],
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
    "house_memberships": {
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
            "roles": [],
            "last_permission_update": str,
            "joined_at": str,
            "house_id": str,
        }
    },
    "house_ids": []
}
}
```

### `HOUSE_JOIN`
[![Source](../assets/images/icons/source_icon.png){: width=28px align=top} Source Code · ](https://github.com/FrostbyteSpace/openhiven.py/)
[Docs · `async def on_house_join()`]()

```json
op: 0,
d: {
  rooms: room[{
    type: int,
    recipients: null
    position: int,
    permission_overrides: bits,
    owner_id: string,
    name: string,
    last_message_id: string,
    id: string,
    house_id: string,
    emoji: object,
    description: string,
    default_permission_override: int
  }],
  roles: role[{
    position: int,
    name: string,
    level: int,
    id: string,
    deny: bits,
    color: string,
    allow: bits
  }],
  owner_id: string,
  name: string,
  members: [{
    user_id: string,
    user: {
      username: string,
      user_flags: string,
      name: string,
      id: string,
      icon: string,
      header: string,
      presence: string
    },
    roles: array,
    last_permission_update: string,
    joined_at: string,
    house_id: string
  }],
  id: string,
  icon: string,
  entities: [{
    type: int,
    resource_pointers: [{
      resource_type: string,
      resource_id: string
    }],
    position: int,
    name: string,
    id: string
  }],
  default_permissions: int,
  banner: string
}
```

### `HOUSE_LEAVE`

```json
op: 0,
d: {
  id: string,
  house_id: string
}
```

### `BATCH_HOUSE_MEMBER_UPDATE`

```json
op: 0,
d: {
  house_id: string;
  batch_type: list;
  batch_size: int;
  data: {
    [resource_id: string]: HouseMember
  }
}
```

### `RELATIONSHIP_UPDATE`

```json
op: 0
d: {
  user: {
    website: string,
    username: string,
    user_flags: int,
    name: string,
    location: string,
    id: string,
    icon: string,
    bio: string
  },
  type: int,
  recipient_id: string,
  id: string
}
```

### `MESSAGE_CREATE`

```json
op: 0
d: {
  timestamp: int,
  room_id: string,
  mentions: [{
    username: string,
    user_flags: string,
    name: string,
    id: string,
    icon: string,
    header: string,
    presence: string,
    bot: boolean
  }],
  member: {
    user_id: string,
    user: {
      username: string,
      user_flags: string,
      name: string,
      id: string,
      icon: string,
      header: string,
      presence: string
    },
    roles: array,
    last_permission_update: string,
    joined_at: string,
    house_id: string
  },
  id: string,
  house_id: string,
  exploding_age: int,
  exploding: boolean,
  device_id: string,
  content: string,
  bucket: int,
  author_id: string,
  author: {
    username: string,
    user_flags: string,
    name: string,
    id: string,
    icon: string,
    header: string,
    presence: string
  }
  attachment: {
    media_url: string,
    filename: string,
    dimensions: {
      width: int,
      type: string,
      height: int
    }
  }
}
```

### `MESSAGE_DELETE`

```json
op: 0
d: {
    room_id: string,
    message_id: string,
    house_id: string
}
```

### `MESSAGE_UPDATE`

```json
op: 0
d: {
  type: int,
  timestamp: string,
  room_id: string,
  metadata: unknown,
  mentions: [{
    username: string,
    user_flags: string,
    name: string,
    id: string,
    icon: string,
    header: string,
    presence: string
  }],
  id: string,
  house_id: string,
  exploding_age: int,
  exploding: boolean,
  embed: object,
  edited_at: string,
  device_id: string,
  content: string,
  bucket: int,
  author_id: string,
  attachment: {
    media_url: string,
    filename: string,
    dimensions: {
      width: int,
      type: string,
      height: int
    }
  }
}
```

### `PRESENCE_UPDATE`

```json
op: 0
d: {
  username: string,
  user_flags: string,
  name: string,
  id: string,
  icon: string,
  header: string,
  presence: string
}
```

### `ROOM_CREATE`

```json
op: 0,
d: {
    house_id: string,
    id: string,
    name: string,
    position: int,
    type: int
}
```

### `ROOM_UPDATE`

```json
```

### `ROOM_DELETE`

```json
```

### `HOUSE_MEMBER_JOIN`

```json
op: 0,
d: {
    house_id: string,
    joined_at: timestamp,
    roles: []
    length: int
    user: {
        id: string,
        name: string,
        user_flags: string,
        username: string,
    }
}
```

### `HOUSE_MEMBER_EXIT`

```json
op: 0
d: {
    id: string,
    house_id: string
}
```

### `HOUSE_MEMBER_ENTER`

```json
op: 0
d: {
  user_id: string,
  user: {
      username: string,
      user_flags: string,
      name: string,
      id: string,
      icon: string,
      bot: bool,
  },
  roles: [],
  presence: string,
  last_permission_update: null,
  joined_at: string,
  id: string,
  house_id: string
}
```

### `HOUSE_MEMBER_UPDATE`

```json
op: 0
d: {
  user_id: string,
  user: {
    website: string,
    username: string,
    user_flags: int,
    name: string,
    location: string,
    id: string,
    icon: string,
    header: string,
    email_verified: boolean,
    bot: boolean,
    bio: string
  },
  roles: object[],
  presence: string,
  last_permission_update: unknown,
  joined_at: string,
  id: string,
  house_id: string
}
```

### `HOUSE_MEMBERS_CHUNK`

```json
op: 0
d: {
  members: {
    id: {
      user_id: string,
      user: {
        username: string,
        user_flags: string,
        name: string,
        id: string,
        icon: string,
        header: string,
        presence: string
      },
      roles: array,
      last_permission_update: string,
      joined_at: string,
      house_id: string
    }
  },
  house_id: string
}
```
        
### `TYPING_START`

```json
op: 0
d: {
  timestamp: int,
  room_id: string,
  house_id: string,
  author_id: string
}
```

### `HOUSE_ENTITY_UPDATE`

```json
op: 0
d: {
  house_id: string,
  entities: [{
    type: int,
    resource_pointers: [{
      resource_type: string,
      resource_id: string
    }],
    position: int,
    name: string,
    id: string
  }]
}
```

### `HOUSE_DOWN`

```json
op: 0
d: {
  unavailable: boolean,
  house_id: string
}
```
