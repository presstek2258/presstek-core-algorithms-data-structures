# basic lambda usage
value = 5
func = lambda x: 2*x
print(f"{value = }")
print(f"{func(value) = }\n")

# map filter and reduce
# these are used to efficiently apply functions 
# to arrays / lists
#
# the functions return an iterable -> use list()

arr = [1,2,3,4,5]
print(f"{arr = }\n")

# map applies a function to every element
# return a list
print(f"{list(map(lambda x: 2*x, arr)) = }")
print(f"{list(map(lambda x: x-1, arr)) = }")

# can also been done with conditions:
# generally preffered (unless lazy loading is desired)
print(f"{[2*x for x in arr] = }")
print(f"{[x-1 for x in arr] = }\n")

# applies a condition to every element
# drops those that dont meet the condition
# returns a list
print(f"{list(filter(lambda x: x>3, arr)) = }")
print(f"{list(filter(lambda x: x%2==0, arr)) = }")

# can also been done with conditions:
# generally preffered (unless lazy loading is desired)
print(f"{[x for x in arr if x>3] = }")
print(f"{[x for x in arr if x%2==0] = }\n")

# applies a function to every element sequentially
# at each step x is the current value
# at each step y is the next value
# returns a single value
from functools import reduce
print(f"{reduce(lambda x,y: x+y, arr) = }")
print(f"{reduce(lambda x,y: x*y, arr) = }\n")



