
# This will work only on list.. but in prods the inputs are steams not lists.. so need to find general approach
# def batched(iterable,n):
#     for i in range(0, len(iterable), n):
#         yield iterable[i:i+n]
# for batch in batched([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3):
#     print(batch)

#2
def batched(iterable,n):
    batch = []

    for item in iterable:
            batch.append(item)
            if len(batch) == n:
                  yield batch
                  batch = []
    if batch:
          yield batch

for batch in batched([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3):
    print(batch)

print("---")        
def big_stream():
    for i in range(1, 11):
        yield i

for batch in batched(big_stream(), 3):
    print(batch)

    
        
        

