# Techie

A simple web tech blog web application built with python(flask).

## Features
- Login and registration
- Add new blog post
- Edit blog post
- Authorization using `OPAL`

## Technologies
- Python (Flask)
- sqlite
- OPAL

## Demo

[Watch the demo video](https://github.com/mehedihasan2810/techie/assets/117534561/7ce468bf-e404-4104-8b9c-97fbc054b9ab)

## Authorization using `OPAL`
The policy permit statement for different roles of users defined `rbac.rego` file

```bash
package app.rbac

# By default, deny requests
default allow = false

# Check if user is admin
user_is_admin {
    input.user.role == "admin"
}

# Check if user is guest
user_is_guest {
    input.user.role == "guest"
}
```

The middlewares that handle authorization using `OPAL` can be found in the `/techie/middleware.py` file

```py
from functools import wraps

import requests

from flask import request

# Admin authorization decorator middleware
def adminAuthorization(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print(request)

         # Create the input for the policy
        input_data = {
            "user": {
                "role": "admin"
            },
        }

        # Call authorization service
        # In the request body, we pass the relevant request information
        response = requests.post('http://localhost:8181/v1/data/app/rbac/user_is_admin', json={
            "input": input_data
        })

        result = response.json().get('result')

        # If the decision is not Allow, we return a 403
        if not result:
            return 'Access Denied', 403
        
        return f(*args, **kwargs)
    
    return decorated



# Guest authorization decorator middleware
def guestAuthorization(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print(request)

         # Create the input for the policy
        input_data = {
            "user": {
                "role": "guest"
            },
        }

        # Call authorization service
        # In the request body, we pass the relevant request information
        response = requests.post('http://localhost:8181/v1/data/app/rbac/user_is_guest', json={
            "input": input_data
        })

        result = response.json().get('result')

        # If the decision is not Allow, we return a 403
        if not result:
            return 'Access Denied', 403
        
        return f(*args, **kwargs)
    
    return decorated
```

