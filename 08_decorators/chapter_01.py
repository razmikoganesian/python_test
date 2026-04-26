from functools import wraps

# DECORATORS
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before fuction run")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from code")

greet()
print(greet.__name__) # will return WRAPPER