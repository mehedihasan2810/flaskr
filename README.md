# Techie

This is a tech blog web application built with Python (Flask) and SQLite for the database. It uses Opal for user authorization. Users can register, log in, log out, and manage blog posts. The app allows creating, editing, and deleting blog posts.

## Features
- Login and registration
- Add new blog post
- Edit blog post
- Delete blog post
- Authorization using `OPAL`

## Technologies
- Python (Flask)
- sqlite
- OPAL

## Demo

[Watch the demo video](https://github.com/mehedihasan2810/techie/assets/117534561/7ce468bf-e404-4104-8b9c-97fbc054b9ab)

## Authorization using `OPAL`
The policy permit statement for different roles of users defined in `rbac.rego` file

`rbac.rego`
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

`/techie/middleware.py`
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

## Getting Started

### Prerequisites

Make sure you have the following packages installed

- Python 3.x
- pip (Python package installer)
- Docker
- docker-compose

### Installation

1. **First, Clone the repo and go to the project folder**
```bash
git clone https://github.com/mehedihasan2810/techie.git
cd techie
```

2. **Create a virtual environment**

- On `macOS/Linux`
```bash
python3 -m venv .venv
```

- On `Windows`
```bash
py -3 -m venv .venv
```

3. **Activate the virtual environment**

- On `macOS/Linux`
```bash
. .venv/bin/activate
```

- On `Windows`
```bash
.venv\Scripts\activate
```

4. **Install the dependencies**
```bash
pip install -r requirements.txt
```

5. **Initialize the Database File**
```bash
flask --app techie init-db
```

6.  **Now spin up the `OPAL` authorization system by running the docker compose file**
```bash
docker-compose up
```

7. **Open another terminal window and follow the `2 and 3 steps` to create and activate the virtual environment in that terminal too then run our blog application by executing the below command**
```bash
flask --app techie run --debug
```

8. Open your browser and visit
```bash
http://127.0.0.1:5000/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository

2. Clone the repo
```bash
git clone https://github.com/mehedihasan2810/techie.git
```
3. Create a new branch
```bash
git checkout -b feature/fix-bug
```
4. Make your changes

5. Stage, commit and push your changes
```bash
git add .
git commit -m 'feat: add feature'
git push origin feature/fix-bug
```
7. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<br>
<br>

Please give a star. Thanks.

