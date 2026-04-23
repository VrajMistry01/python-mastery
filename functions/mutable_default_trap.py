'''This program shows the mutable default argument trap and the correct fix.''' 

def append_to(item, bucket=[]):

    """The def evaluates defaults once and stores them on the function object. 
        Each call binds bucket  to that same shared heap object. .append mutates in place — same address, new contents. 
        Local names die when the frame pops; the heap object survives because something outside 
        (the return value, the __defaults__) still references it."""
        
    bucket.append(item)
    return bucket

x = append_to("a")
print('BEFORE')
print(x)
y=append_to("b")
print('AFTER')
print(x)
print(y)
print(x is y)