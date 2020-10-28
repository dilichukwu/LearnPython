print("\n9.1----------------------------------------------------------------------------------------")


# 9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
def good():
    return ["Harry", "Ron", "Hermione"]


print(good())

print("\n9.2----------------------------------------------------------------------------------------")


# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10).
# Use a for loop to find and print the third value returned.
def get_odds():
    for num in range(1, 10):
        if num % 2 == 1:
            yield num


count = 1
for i in get_odds():
    if count == 3:
        print(i)
    count += 1

print("\n9.3----------------------------------------------------------------------------------------")


# 9.3 Define a decorator called test that prints 'start' when a function is called, and 'end' when it finishes.
def test(func):
    def inner(*args, **kwargs):
        print('Start')
        value = func(*args, **kwargs)
        print('End')

        return value

    return inner


@test
def add2(a, b):
    return a + b


# print(test(add2)(3, 5))
print(add2(3.2, 6.8))


def test2(msg):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(msg)
            print('Start')
            value = func(*args, **kwargs)
            print('End')
            return value

        return inner

    return wrapper


@test2(msg='Sent my love!!!')
def add3(a, b, c):
    return a + b + c


# print(test2("Sending my love...")(add3)(1,2,3))
print(add3(3.2, 4.3, 5.5))

print("\n9.4----------------------------------------------------------------------------------------")


# 9.4 Define an exception called OopsException. Raise this exception to see what happens.
# Then, write the code to catch this exception and print 'Caught an oops'.
class OopsException(Exception):
    def __init__(self):
        super().__init__('Oops! Exception occurred. You were caught by surprise!'+'\U0001F632\U0001F632\U0001F632')


try:
    raise OopsException()
except Exception as oops:
    print(oops)
