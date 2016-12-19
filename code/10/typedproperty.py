# typedproperty.py

def typed_property(name, expected_type):
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('Expected {}'.format(
                    expected_type))
        setattr(self, private_name, value)

    return prop

Integer = lambda name: typed_property(name, int)
Float = lambda name: typed_property(name, float)
String = lambda name: typed_property(name, str)

class Holding(object):
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

