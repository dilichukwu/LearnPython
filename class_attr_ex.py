# An object inherits (references) a class variable, if it does not have a variable of same name
# Any modification made to the class variable reflects on the object
# Any assignment operation by an object that involves an existing class variable overrides (shadows)
# the class variable
# If += is used, the initial value of the class variable is used (retrieved) before the override takes place
# Once overriding takes place, updates to the class variable no longer reflects on the object variable value
# This is because the object now has it's own variable (count) and now longer references the class variable
# A class cannot access object method or data
# It is legal to define more than one method of the same name in a class, but only the last method will
# be called

class Fruit:
    count = -3  # objects created initially reference count

    @classmethod
    def incr(cls):
        cls.count += 1

    def incr(self):  # once method is called, an object variable count is created.
        self.count += 7  # class count value -3 read, then new count for object created. self.count = -3+7
        # To update the class variable count, use Fruit.count += 7

fruit = Fruit()
print(fruit.count)
print(Fruit.count)
fruit.incr()
Fruit.incr(Fruit)
print(fruit.count)
print(Fruit.count)
