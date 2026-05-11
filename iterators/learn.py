# nums = iter([1, 2, 3])
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# def count_up_to(n):
#     i = 1               # ← first call sets this
#     while i <= n:
#         yield i         # ← pauses here; resumes here on next() call
#         i += 1

# gen = count_up_to(3)    # creates generator, body NOT run yet
# print(type(gen))
def foo():
    print("A")
    yield 1

print("BEFORE")
g = foo()
print("AFTER GENERATOR CREATED")
print("BEFORE NEXT")
next(g)
print("AFTER NEXT")

def gen():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")

g = gen()
print(next(g))
print(next(g))