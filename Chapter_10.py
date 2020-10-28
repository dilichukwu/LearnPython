print("\n10.1--------------------------------------------------------------------------------------")


# 10.1 Make a class called Thing with no contents and print it. Then, create an object called example
# from this class and also print it. Are the printed values the same or different?
class Thing:
    pass


print(Thing)

example = Thing()
print(example)

print("\n10.2--------------------------------------------------------------------------------------")


# 10.2 Make a new class called Thing2 and assign the value 'abc' to a class attribute called letters. Print letters.
class Thing2:
    letters = 'abc'


print(Thing2.letters)

print("\n10.3--------------------------------------------------------------------------------------")


# 10.3 Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance
# (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?
class Thing3:
    def __init__(self):
        self.letters = 'xyz'


obj = Thing3()
print(obj.letters)

print("\n10.4--------------------------------------------------------------------------------------")


# 10.4 Make a class called Element, with instance attributes name, symbol, and number. Create an object of this
# class with the values 'Hydrogen', 'H', and 1.
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


element = Element('Hydrogen', 'H', 1)
print('element: ', element)

print("\n10.5--------------------------------------------------------------------------------------")
# 10.5 Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1.
# Then, create an object called hydrogen from class Element using this dictionary.
h_dict = dict(name='Hydrogen', symbol='H', number=1)
hydrogen = Element(h_dict['name'], h_dict['symbol'], h_dict['number'])
print('hydrogen:', hydrogen)

print("\n10.6--------------------------------------------------------------------------------------")


# 10.6 For the Element class, define a method called dump() that prints the values of the object’s attributes
# (name, symbol, and number).
# Create the hydrogen object from this new definition and use dump() to print its attributes.
class Element2:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print("(name=", self.name, ", symbol=", self.symbol, ", number=", self.number, ")", sep="")


hydrogen = Element2('Hydrogen', 'H', 1)
hydrogen.dump()

print("\n10.7--------------------------------------------------------------------------------------")
# 10.7 Call print(hydrogen). In the definition of Element, change the name of the method dump to __str__,
# create a new hydrogen object, and call print(hydrogen) again.
print(hydrogen)


class Element3(Element2):
    def __str__(self):
        return "(name=" + self.name + ", symbol=" + self.symbol + ", number=" + str(self.number) + ")"


hydrogen = Element3('Hydrogen', 'H', 1)
print(hydrogen)

print("\n10.8--------------------------------------------------------------------------------------")


# 10.8 Modify Element to make the attributes name, symbol, and number private.
# Define a getter property for each to return its value.
class Element4:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


hydrogen = Element4('Hydrogen', 'H', 1)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)
print(dir(hydrogen))

print("\n10.9--------------------------------------------------------------------------------------")


# 10.9 Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats().
# This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe).
# Create one object from each and print what it eats.
class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


def eats(animal):
    print(animal.eats())


for a in [Bear(), Rabbit(), Octothorpe()]:
    print(a.eats())
    eats(a)

print("\n10.10--------------------------------------------------------------------------------------")


# 10.10 Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does().
# This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone).
# Then, define the class Robot that has one instance (object) of each of these.
# Define a does() method for the Robot that prints what its component objects do.
class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class Smartphone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.__laser = Laser()
        self.__claw = Claw()
        self.__smartphone = Smartphone()
        self.collections = [self.__laser, self.__claw, self.__smartphone]

    def does(self):
        for c in self.collections:
            print(c.does())


robot = Robot()
robot.does()

