# a=50
# b=50
# c=500
# d=500
# print(a is b)
# print(c is d)
# a = 50
# b = 50
# print(id(a), id(b), a is b)

# c = 500
# d = 500
# print(id(c), id(d), c is d)

def a():
    a=500
    print(id(a))
    def b():
        b=500
        print(id(b))
        print(a is b)  #Same file → same compilation context → Python optimizes identical literals to one object. Same behavior we saw before.
    return b
a()()