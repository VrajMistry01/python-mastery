def count_calls(func):
    count = 0
    def wrapper(*args,**kwargs):
        nonlocal count
        count+=1
        print(f"{func.__name__} has been called {count} times")
        res = func(*args,**kwargs)
        return res
    return wrapper
@count_calls
def greet(name):
    return f"hi, {name}"


print(greet("vraj"))
print(greet("ravi"))
print(greet("alice"))