#All odd nums for 1-20 using range-

for num in range(1,21):
    if num%2!=0:
        print(num)

#enumerate()

letters =["a","b","c"]
for key,value in enumerate(letters):
    print(key,value)

# Count down using while loop:

timer = 10 

while timer>0:
    print(timer)
    timer = timer-1

'''find required positive number from the list.Skip the negative numbers 
nd find the index of required positvie number'''
# target = 12
target = 10
list_with_errors = [5, -1, 8, 0, 12, 7, 3]

for index,value in enumerate(list_with_errors):
    if value < 0:
        continue
    if value==target:
        print('Found at index',index)
        break
else:
    print('target not present')

# iter()/next() demo- iterating my name😂

name = 'VRAJ'
iterator = iter(name)

while True:
    try:
        x=next(iterator)
        print(x)
    except StopIteration:
        break