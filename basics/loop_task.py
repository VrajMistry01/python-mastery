# Coding task for loops:
# Task: FizzBuzz
# Classic problem. Write a function fizzbuzz(n) that prints numbers from 1 to n, but:

# If divisible by 3, print "Fizz" instead
# If divisible by 5, print "Buzz" instead
# If divisible by both 3 and 5, print "FizzBuzz" instead

# Example for n = 15:
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

def fizzbuzz(n:int):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz') 
        elif i%3==0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')     
        else:
            print(i)

fizzbuzz(15)
