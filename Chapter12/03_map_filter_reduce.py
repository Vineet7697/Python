# map function

li=[1,2,3,4,5]
result=map(lambda x:x*x,li)
print(list(result))



li=[1,2,3,4,5]
square=lambda x:x*x
sqlist=map(square,li)
print(list(sqlist))

li=[1,2,3,4,5]
def square(x):
    return x**2
result=map(square,li)
print(list(result))



# Filter  function
def even(n):
    if n%2==0:
        return True
    return False
onlyEven=filter(even,li)
print(list(onlyEven))

# Reduce function
from functools import reduce
def sum(a,b):
    return a+b
print(reduce(sum,li))