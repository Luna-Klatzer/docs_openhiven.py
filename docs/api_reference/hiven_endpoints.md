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
  "Authorization": "put here your token"
}
```

## Writing a `POST`, `PUT` or `PATCH` Request

Writing a request for one of these Methods is relatively easy with Hiven and only requires you to specify what datatype 
the body you sent is, so the server can properly read it and perform the request. In this case the standard type 
`application/json` is used which allows us to pass regular data in json format to the Server. Throughout the entire API 
this is common usage for endpoints.

!!! info

    After some research, specifying the Content-Type is not required in some cases, but it is nevertheless good practice 
    setting it. Still, if it does more harm than good, you should consider removing it when it is not needed!

To specify this datatype add to the header this line: 
```json
{
  "Content-Type": "application/json"
}
```

After that, you only need to write proper JSON-requests, and it should work like wanted! There are exceptions to that 
of course, since some requests might require some additional information and configuration.

Body-Example for the data:
```json
{
  "data_field": "value"
}
```

!!! warning 

    Specifying the Content-Type can cause errors if you specify it on endpoints that do not expect such datatype which 
    is common in `GET` or `DELETE` where the server expects no data expected, and such specification causes a `400` 
    Exception!

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

    ??? fail "400"

        Authorisation Token is not set or faulty! Check your header if the token was entered correctly!

        **Expected Response:**
        
        ```json
        {
            "success": False,
            "error": {
                "code": "no_auth",
                "message": "Authorization is required for this route"
            }
        }
        ```
    
        *Note that the issue can also be caused by a faulty header-configuration in the set fields like 'Content-Type'*

=== "PATCH"





### House Endpoints


### Message Endpoints


### Room Endpoints 

