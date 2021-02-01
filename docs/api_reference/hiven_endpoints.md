# Hiven Endpoints

---

!!! Warning

    **This documentation page is not finished yet! Information can be outdated or entirely not available!**

The Hiven API uses standard REST endpoints to allow its users to interact with it. Therefore, you can quickly write 
HTTP-requests for these endpoints as long as you specify the details. We will explain this in-depth through-out the
docs for each endpoint.

Current API access-point:

* Host: `api.hiven.io`
* Version: `v1`
* URL: `https://api.hiven.io/v1/`

## Authentication Header

---

The Hiven API uses a classic header authorization where your auth-token is passed as a parameter in the header of the
request. If you do not have your token yet, getting it is discussed in the docs page [Getting a User-token](https://openhivenpy.readthedocs.io/en/mkdocs-material-rewrite/getting_started/deploying_your_first_bot.html#getting-a-user-token)

If you already have one and want to make a request to Hiven simply put it as following into the header:
```json
{
  "Authorization": "enter your token here"
}
```

## Writing a Request with json-body

### Specifying the Content-Type

Writing a request that contains data is relatively easy with Hiven and only requires you to specify what datatype 
the body you sent is, so the server can properly read it and perform the request. In this case the standard type 
`application/json` is used which allows us to pass regular data in json format to the Server. Throughout the entire API 
this is common usage for endpoints.

!!! info

    After some research, specifying the Content-Type is not required in some cases, but it is nevertheless good practice 
    setting it. Still, if it does more harm than good, you should consider removing it when it is not needed!

To specify the `application/json` datatype, add to the header this line: 
```json
{
  "Content-Type": "application/json"
}
```

### Writing a json-body

After the content-type was specified, and the configuration works, you only need to write a proper JSON-body, and it 
should work like wanted! There are exceptions to that of course, since some requests might require some additional 
information and configuration.

Body-Example:
```json
{
  "data_field": "value"
}
```

!!! warning 

    Specifying the Content-Type can cause errors if you set it on endpoints that do not expect such datatype which 
    is often the case with the methods `GET` or `DELETE` where the server usually expects no data, and such specification
    causes a `400 Bad Request` HTTP-Exception!

    **Common-Methods for data parsing:**
    
    * `POST`
    * `PUT`
    * `PATCH` 

## Endpoints

---

### User Endpoints

#### ```/users/@me```

Default user endpoint for accessing the user-data of the owner of the passed token in the header.

=== "GET"

    ??? success "200"

        Authorisation was successful and the body contains the requested data

        **Expected Response:**

        ```json
        {
            "success": true,
            "data": {
                "id": str,
                "name": str,
                "username": str,
                "icon": str,
                "header": str,
                "user_flags": int,
                "bot": bool,
                "location": str,
                "website": str,
                "bio": str,
                "email": str,
                "email_verified": bool,
                "mfa_enabled": bool
            }
        }
        ```

    ??? fail "400"

        Authorisation Token is not set or faulty! Check your header if the token was entered correctly!

        **Expected Response:**
        
        ```json
        {
            "success": false,
            "error": {
                "code": "no_auth",
                "message": "Authorization is required for this route"
            }
        }
        ```

=== "PATCH"

    ??? success "200"

        Patch was successful and the data was changed! The response will containt the updated data of the User

        ```json
        {
            "success": True,
            "data": {
                "id": str,
                "name": str,
                "username": str,
                "icon": str,
                "header": str,
                "user_flags": int,
                "bot": bool,
                "location": str,
                "website": str,
                "bio": str,
                "email": str,
                "email_verified": bool,
                "mfa_enabled": bool
            }
        }
        ```

        !!! warning 
        
            If you enter an unknown or mistyped variable, it will not be correctly recognised, and the Hiven API Server 
            will change no value. Still the result will be 200 and the user-data will be sent without any changes!

    ??? fail "400"

        Authorisation Token is not set or faulty! Check your header if the token was entered correctly!

        **Expected Response:**
        
        ```json
        {
            "success": false,
            "error": {
                "code": "no_auth",
                "message": "Authorization is required for this route"
            }
        }
        ```

        !!! Warning

            Currently there is a bug in the Hiven API causing it to return 200 instead of 400 or 403!

    ??? fail "415"

        The passed content-type is faulty!
    
        **Expected Response:**
    
        ```json
        {
            "success": false,
            "error": {
                "code": "internal_server_error",
                "message": "Something went wrong interally"
            }
        }
        ```

#### ```/streams/@me/mentions```

Endpoint for fetching your mentions in the Houses and rooms of your scope.

=== "GET"
    
    ??? success "200"
    
        Returns a list with all mentions wrapped in a message Hiven object
    
        **Expected Response:**
    
        ```json
        {
            "success": true,
            "data": [
            {
                "room_id": str,
                "bucket": int,
                "id": str,
                "attachment": unknown,
                "author_id": str,
                "content": str,
                "device_id": str,
                "edited_at": str,
                "embed": {},
                "exploding": bool,
                "exploding_age": unknown,
                "mentions": [
                    {
                        // User object
                        "icon": str,
                        "id": str,
                        "username": str,
                        "name": str,
                        "header": str,
                        "user_flags": str,
                        "bot": bool
                    }
                    // All mentions in the message
                ],
                "metadata": unknown,
                "timestamp": str,
                "type": int,
                "author": {
                    // User object
                    "icon": str,
                    "id": str,
                    "username": str,
                    "name": str,
                    "header": str,
                    "user_flags": str,
                    "bot": bool
                }
            },
            ...
            ]
        }
        ```

    ??? fail "400"

        Authorisation Token is not set or faulty! Check your header if the token was entered correctly!

        **Expected Response:**
        
        ```json
        {
            "success": false,
            "error": {
                "code": "no_auth",
                "message": "Authorization is required for this route"
            }
        }
        ```

        !!! Warning

            Currently there is a bug in the Hiven API causing it to return 200 instead of 400 or 403!

### House Endpoints


### Message Endpoints


### Room Endpoints 

## Exceptions

### `400 Bad Request` - no_auth

If you receive this error response that means it is an issue relating the authentication which is either not passed 
in the headers or is not correct!

More info on [`Authentication Header`](#authentication-header)

**Example Exception Response:**

```json
    {
        "success": false,
        "error": {
            "code": "no_auth",
            "message": "Authorization is required for this route"
        }
    }
```

### `404 Not Found` - not_found

The 404 Exception is a classic exception in the Web-Area and means here the Hiven API did not find the endpoint you
specified.

**Example Exception Response:**

```json
{
    "success": false,
    "error": {
        "code": "not_found",
        "message": "Not found"
    }
}
```

### `415 Unsupported Media Type` - internal_server_error
    
If you receive this error, the server encountered an internal error due to a header-issue where some data that you 
passed, or a specification causes the server to fail to perform the request.

**Example Exception Response:**

```json
{
    "success": false,
    "error": {
        "code": "internal_server_error",
        "message": "Something went wrong interally"
    }
}
```