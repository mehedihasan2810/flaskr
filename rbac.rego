package app.rbac

# By default, deny requests
default allow = false

# Allow access if user is an admin
allow {
    input.user.role == "admin"
}
