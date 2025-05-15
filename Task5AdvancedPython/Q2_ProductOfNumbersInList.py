'''Given a list of numbers, use the reduce function
and lambda expression to find the product of all the numbers '''

# importing python inbuilt method reduce from functools
from functools import reduce

numList = [3, 5, 11, 4, 2, 9]

# Finding the product of all numbers in the list using reduce(function, iterable)
productOfAllNumbers = reduce(lambda x, y: x * y, numList)

print(f"Product of all numbers in given list {numList} is: {productOfAllNumbers}")
