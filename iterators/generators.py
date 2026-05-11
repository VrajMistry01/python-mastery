def squares(n):
    i=1
    while i<=n:
        yield i**2
        i+=1

for s in squares(5):     # ← this should just work
    print(s)