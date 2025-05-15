'''Write a list comprehension that creates a new list of squares of even numbers in a list.
Use lambda expression to find even numbers in the list'''

numList = [3, 6, 9, 12, 15, 18, 21, 5, 10, 15]

# Filter out the even numbers from the given list
evenNumberList = filter(lambda x: x % 2 == 0, numList)

# Create a list for squares of evenNumberList
squareOfEvenNumbersList = [num * num for num in evenNumberList]
print(f"List of squares of even numbers in given list is: {squareOfEvenNumbersList}")

'''For self understanding the same program without using lambda and list comprehension
squareList = []
for x in numList:
    if x%2==0:
        square = x*x
        squareList.append(square)
print(squareList)
'''
