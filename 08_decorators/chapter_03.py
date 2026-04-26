from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied! For admins only")
            return None
        else : 
             return func(user_role)
    return wrapper
    
@require_admin
def access_inventory(role):
    print(f"Access granted to {role}")

access_inventory("admin")
access_inventory("user")