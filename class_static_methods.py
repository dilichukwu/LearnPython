# No need to create objects in order to call class or static methods
# Technically both staticmethod and classmethod can be overriden by an object's instance method
# You can define object-only methods within class instance methods using self.methodname = afunction
# You can also define object-only methods after object creation e.g. car.methodname = afunction
# You can nest function definitions within functions

class Car:
    __count = 0

    def __init__(self):
        Car.__count += 1
        self.unique_data = 'ID: ' + str(id(self))
        self.unique_obj_method = lambda : '***'+str(id)+'***'

        def x():
            return 'Malcolm X'
        self.x = x

    def unique_attr(self):
        return id(self)

    @classmethod
    def object_count(cls):
        return cls.__count

    @staticmethod
    def automobile_history():
        return \
            'The history of automobile began in the second half of the 19th century with the development ' \
            'of the first internal combustion engine by Carl Benz, in Germany'


print(Car.automobile_history())
print(Car.object_count())

car = Car()
print(car.unique_attr())
print(car.unique_data)
print(car.unique_obj_method)
print(car.x())

car.automobile_history = lambda: 'No history'
print(car.automobile_history())

print(Car.unique_attr(Car))

