# sample.py

from logcall import logformat

logged = logformat('YOU ARE CALLING {func.__name__}')

@logged
def add(x, y):
    '''
    Adds x and y
    '''
    return x + y

@logged
def sub(x, y):
    return x - y

@logged
def mul(x, y):
    return x * y
