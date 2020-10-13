def decorator(func):
    def params(*args, **kwargs):
        print('x:', args[0])
        print('y:', args[1])
        return func(*args, **kwargs)
    return params

@decorator
def adder(x, y):
    return x + y

print(adder(2,5))