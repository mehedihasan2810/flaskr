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
