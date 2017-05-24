# logcall.py

from functools import wraps

def logged(func):
    # Idea: Give me a function, I'll put logging
    # around it

    print('Adding logging to', func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('You called', func.__name__)
        return func(*args, **kwargs)

    return wrapper
