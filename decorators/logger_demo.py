def logger(func):
    def wrapper(*args,**kwargs):
        print(f"ENTER {func.__name__} with args={args} and kwargs={kwargs}")
        result = func(*args,**kwargs)
        print(f"EXIT {func.__name__} returned {result}")
        return result
    return wrapper


@logger
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(f"caller got: {result}")