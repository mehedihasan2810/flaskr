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