"""
This script contains a decorator that allows running the decorated function
only with a specified role. This is a provisional setup. Preserves metadata.
Roles are checked at runtime, not at function creation time. At function
creation time the roles specified in the decorator factory are validated.
"""

from enum import Enum, auto
from functools import wraps

# XXX Below the implementation of roles is provisional and does not serve
#       as a proper example. It is only to write a decorator.

class Role(Enum):
    ADMIN = auto()
    USER = auto()
    NOT_SET = auto()

CURRENT_ROLE = Role.NOT_SET

def set_role(new: Role):
    if not isinstance(new, Role):
        raise TypeError("Role type required.")
    global CURRENT_ROLE
    CURRENT_ROLE = new


def access(*roles):
    if not roles:
        raise ValueError("At least one role must be specified.")

    if any(not isinstance(r, Role) for r in roles):
        raise TypeError("Invalid role passed into the decorator.")

    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if CURRENT_ROLE not in roles:
                raise PermissionError("Invalid access.")
            return func(*args, **kwargs)
        return wrapper
    return dec


@access(Role.ADMIN, Role.USER)
def hello_user(name):
    print(f"Hello user {name}!")

@access("admin")
def hello_admin(name):
    print(f"Hello user {name}!")

if __name__ == "__main__":
    set_role(Role.USER)
    print()

    try:
        print("Trying user hello as user.")
        hello_user("user")
    except PermissionError:
        print("No user role.")

    try:
        print("Trying admin hello as user.")
        hello_admin("user")
    except PermissionError:
        print("No admin role.")


    set_role(Role.ADMIN)

    try:
        print("Trying user hello as admin.")
        hello_user("admin")
    except PermissionError:
        print("No user role.")

    try:
        print("Trying admin hello as admin.")
        hello_admin("admin")
    except PermissionError:
        print("No admin role.")
