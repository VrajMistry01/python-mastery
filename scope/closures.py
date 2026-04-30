"""
closures.py — canonical demonstration of Python closures.

A closure is a function that remembers values from the scope where it
was created, even after that scope is gone.

This file shows:
  1. Read-only closure (LEGB walks)
  2. Inspecting the closure backpack
  3. Modifying captured state with `nonlocal`
  4. Mutation vs reassignment distinction
"""


# 1. Read-only closure — `inner` captures `name` from `outer`.
def make_greeter(greeting):
    def greet(person):
        return f"{greeting}, {person}"
    return greet


hello = make_greeter("hello")
namaste = make_greeter("namaste")

print(hello("vraj"))         # hello, vraj
print(namaste("ravi"))       # namaste, ravi


# 2. Inspecting the closure backpack.
print("\n--- closure inspection ---")
print("captured names :", hello.__code__.co_freevars)        # ('greeting',)
print("cell contents  :", hello.__closure__[0].cell_contents) # 'hello'


# 3. Modifying captured state — `nonlocal`.
def make_counter():
    count = 0
    def increment():
        nonlocal count       # without this: UnboundLocalError
        count += 1
        return count
    return increment


counter = make_counter()
print("\n--- counter ---")
print(counter())             # 1
print(counter())             # 2
print(counter())             # 3


# 4. Mutation does NOT need `nonlocal`. Reassignment does.
def append_via_mutation():
    items = []
    def inner():
        items.append(1)      # mutating the list — no assignment to `items`
    inner()
    return items


def append_via_reassignment_broken():
    items = []
    def inner():
        items = items + [1]  # ASSIGNMENT — `items` becomes local to inner
    inner()
    return items


print("\n--- mutation vs reassignment ---")
print("mutation works            :", append_via_mutation())
# print("reassignment crashes      :", append_via_reassignment_broken())  # uncomment to see UnboundLocalError