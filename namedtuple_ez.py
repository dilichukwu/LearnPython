from collections import namedtuple

"""To recap, here are some of the pros of a named tuple:
It looks and acts like an immutable object.
It is more space and time efficient than objects.
You can access attributes by using dot notation instead of dictionary-style square brackets.
You can use it as a dictionary key.
"""

Engine_ = namedtuple('Engine', 'horsepower brand year')
engine = Engine_(horsepower=10, brand='Perkins', year='2018')
for x in engine:
    print(x)

class Engine:
    def __init__(self):
        self.horsepower = 20
        self.brand = 'Lister'
        self.year = 2019

eng = Engine()
for x,y in (vars(eng)).items():
    print(x,":",y)

#del eng.year

for x in dir(eng):
    print (x)

