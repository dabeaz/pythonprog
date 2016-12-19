# sample.py

from logcall import logformat, logmethods

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

@logmethods
class Spam(object):
    def __init__(self, value):
        self.value = value

    def yow(self):
        print('Yow!')
        
    def grok(self):
        print('Grok!')


