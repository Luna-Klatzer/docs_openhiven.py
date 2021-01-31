# Hiven Endpoints

---

!!! Warning

    **This documentation page is not finished yet! Information can be outdated or entirely not available!**


## Authentication Header

---

## User Endpoints

---

### ```/users/@me```

Default user endpoint for accessing the user-data of the owner of the passed token in the header.

=== "GET"

    ??? success "200"

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



        

## House Endpoints

---

## Message Endpoints

---

## Room Endpoints 

---
