
class Shape:
    def __init__(self, atype=None):
        self.type_ = atype

    def get_type(self):
        return self.type_

    def set_type(self, atype):
        self.type_ = '.' + atype + '.'

    type = property(get_type, set_type)

shape = Shape('Circle')
shape.type = 'Triangle'
print(shape.type)



