# Once you define getter and setter using annotations, you cannot call the methods as normal; you have
# to reference them as variables. This also applies when calling from within the class methods

class Shape:
    def __init__(self, num_sides):
        self.type = num_sides

    @property
    def type(self):
        if self._numofsides == 0:
            return 'Point'
        if self._numofsides == 1:
            return 'Straight Line'
        if self._numofsides == 3:
            return 'Triangle'
        if self._numofsides == 4:
            return 'Rectangle'
        if self._numofsides > 4:
            return 'Polygon'

        return 'Unknown Shape'

    @type.setter
    def type(self, num_sides):
        self._numofsides = num_sides


shape = Shape(6)
print(shape.type)
#shape.numofsides=1
#print(shape.type)
#print(shape._Shape__obfuscate)
print(vars(shape))

