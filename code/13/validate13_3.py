# validate.py

class Typed(object):
    expected_type = object

    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected {}'.format(self.expected_type))
        instance.__dict__[self.name] = value

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

def typed(cls):
    cls._attributes = set()
    for key, val in vars(cls).items():
        if isinstance(val, Typed):
            val.name = key
    return cls

def validate(**kwargs):
    def decorate(cls):
        for name, val in kwargs.items():
            setattr(cls, name, val(name))
        return cls
    return decorate

class structuretype(type):
    def __new__(meta, name, bases, methods):
        cls = super().__new__(meta, name, bases, methods)
        cls = typed(cls)
        return cls

class Structure(metaclass=structuretype):
    def __setattr__(self, name, value):
        if name not in self._attributes:
            raise AttributeError('No attribute {}'.format(name))
        super().__setattr__(name, value)

class Holding(Structure):
    name = String()
    date = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

