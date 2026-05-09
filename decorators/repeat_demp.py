def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"call {i+1}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def add(a, b):
    return a + b


result = add(2, 3)
print(f"final result: {result}")