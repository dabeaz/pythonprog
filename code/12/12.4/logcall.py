# logcall.py

from functools import wraps

def logformat(fmt):
    def logged(func):
        # Idea: Give me a function, I'll put logging
        # around it

        print('Adding logging to', func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)

        return wrapper
    return logged

logged = logformat('You called {func.__name__}')


def logmethods(cls):
    for key, value in list(vars(cls).items()):
        if callable(value):
            # Is it a method? If so, decorate
            setattr(cls, key, logged(value))
    return cls
