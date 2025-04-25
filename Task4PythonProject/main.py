'''Question 1: [10,501,22,37,100,999,87,351]
Create 2 list. One with even numbers and another with odd numbers from the above list'''

print("Question 1: [10,501,22,37,100,999,87,351], create odd and even number lists")

# Defining list variable for the list given in the question
givenList = [10, 501, 22, 37, 100, 999, 87, 351]

# initializing empty even and odd lists
evenNumberList = []
oddNumberList = []

# Iterating the givenList using for loop
for i in range(len(givenList)):

    # finding that the current element in the list is even by using %
    if givenList[i] % 2 == 0:
        # adding the even numbers to the evenNumberList when the above if condition is success.
        evenNumberList.append(givenList[i])

    # If the above condition fails, then adding the numbers to the oddNumberList
    else:
        oddNumberList.append(givenList[i])

# Printing the even and odd number lists.
print("Even number list: ", evenNumberList)
print("Odd number list: ", oddNumberList)

'''Question 2: [10,501,22,37,100,999,87,351]
Count all the prime numbers
and create a new list with all prime numbers from the given list'''

print("Question 2: Create list with prime numbers from [10,501,22,37,100,999,87,351] ")
# defining the list given in the question
givenList = [10, 501, 22, 37, 100, 999, 87, 351]

# Initializing a prime number list
primeNumberList = []

# Iterating each element in the givenList
for i in range(len(givenList)):

    '''Finding prime number by dividing the given number by
     all the numbers in range from 2 till the given number'''
    for x in range(2, givenList[i]):

        ''' Check that the given number is dividable by any of the number between 2 till the given number.
        If yes, then the given number is not prime. Exit the loop and move to next number from the list'''
        if givenList[i] % x == 0:
            break

        ## If no, Add the number to the prime number list and exit the loop and move to next element in the list
        else:
            primeNumberList.append(givenList[i])
            break

# printing the prime number list and the number of prime numbers present in the given list
print("Prime number list is ", primeNumberList)
print(f"Count of prime numbers in the list is: {len(primeNumberList)}")

'''Question 3: Find out happy numbers: [10, 501, 22, 37, 100, 999, 87, 351]'''

print("Question 3: Find out happy numbers: [10, 501, 22, 37, 100, 999, 87, 351]")
# defining the list given in the question
givenList = [10, 501, 22, 37, 100, 999, 87, 351]

'''Initializing list variables
happyNumList is to store happy numbers 
subNumList to store the numbers created during happy number flow check. If the number is already existing in this sublist,
then we can conclude the numbers repeating in a loop and not getting 1, so the number is not an happy number.
'''
happyNumList = []
subNumList = []

# for loop to iterate each number in the given list to check happy number or not
for num in range(len(givenList)):

    # Initializing sumOfsquare of numbers during each iteration
    sumOfsquareOfNumber = 0
    givenNum = givenList[num]

    # Calculation to find happy number is executed using while loop for each number is not 1 and not in the subNumList
    while givenNum > 0:
        digitsOfGivenNum = str(givenNum)

        # Finding the addition of square of each digit in given number
        for i in range(len(digitsOfGivenNum)):
            sumOfsquareOfNumber += int(digitsOfGivenNum[i]) ** 2

        # Declare the number is Happy number if the sum of squre of each digit in the given number is 1,
        # and reset the sumOfSquareOfNumber to 0 to use it for validating next number in the given list
        if sumOfsquareOfNumber == 1:
            happyNumList.append(givenNum)
            sumOfsquareOfNumber = 0
            break

        # If the sum is not 1, then add the outcome to the subNumList and repeat the process either till getting 1 or
        # till the number in subNumList repeat
        else:
            givenNum = sumOfsquareOfNumber
            sumOfsquareOfNumber = 0
            if givenNum not in subNumList:
                subNumList.append(givenNum)
            else:
                break

    # clearing the subset before moving to the next number in the givenList
    subNumList.clear()
print(f'Happy number list is {happyNumList}')

'''Question 4: find the sum of first and last digit of an integer'''
print("Question 4: find the sum of first and last digit of an integer")
# Get integer input from console
userInput = input("Enter a number with atleast 2 digits:")

# Validate that the userIput has atleast 2 digits to add the first and last digit
if len(userInput) > 1:
    # Get the first digit of the userinput in integer format
    firstDigit = int(userInput[0])
    # Get the last digit of the userinput in integer format
    lastDigit = int(userInput[-1])

    # sum of first and last digit
    sumofFirstAndLastDigits = firstDigit + lastDigit
    print(f'Sum of first and last digits of given number is: {sumofFirstAndLastDigits}')

else:
    print("Given number should have atleast 2 digits")

# Question 5: Find the ways to make Rs 10, using Rs 1, 2, 5, and 10 coins.

print("Question 5: Find the ways to make Rs 10, using Rs 1, 2, 5, and 10 coins")
# Given coins list
coinList = [1, 2, 5, 10]
targetAmount = 10

# Defining empty result list to store the all the possibility combination of coin list to make 10
results = []
i = 1

# Setting up the initial count of Rs.10 coin to 0 and get into the iteration if the total value of Rs.10 coin is less than 10.
noOfCoin10 = 0
while 10 * noOfCoin10 <= targetAmount:

    # Setting up the initial count of Rs.5 coin to 0 and get into the iteration if the total value of Rs.10 and Rs.5 coins are less than 10.
    noOfCoin5 = 0
    while 10 * noOfCoin10 + 5 * noOfCoin5 <= targetAmount:

        # Setting up the initial count of Rs.12 coin to 0 and get into the iteration if the total value of Rs.10,5 and 2 coins are less than 10.
        noOfCoin2 = 0
        while 10 * noOfCoin10 + 5 * noOfCoin5 + 2 * noOfCoin2 <= targetAmount:

            # finding out how many Rs.1 is needed
            countOfCoin1 = targetAmount - (10 * noOfCoin10 + 5 * noOfCoin5 + 2 * noOfCoin2)

            # If no.of Rs.1 is greater than 0
            if countOfCoin1 >= 0:
                # calculate the count of each coin needed
                countOfEachCoin = [1] * countOfCoin1 + [2] * noOfCoin2 + [5] * noOfCoin5 + [10] * noOfCoin10

                # store the result to the results list
                results.append(countOfEachCoin)
                print(f"{i}: {countOfEachCoin}")
                i += 1
            noOfCoin2 += 1
        noOfCoin5 += 1
    noOfCoin10 += 1

print(f"Total unique ways to make {targetAmount} using {coinList}: {len(results)}")

'''Find duplicates in the below 3 lists
[abc, def, ghi, jkl, 1, 2]
[pqr, stu, vwx, abc, 2]
[abc, def, vwx, xyz, 3]
'''
# Given lists
list1 = ['abc', 'def', 'ghi', 'jkl', 1, 2]
list2 = ['pqr', 'stu', 'vwx', 'abc', 2]
list3 = ['abc', 'def', 'vwx', 'xyz', 3]
print(f'Question 6: Find duplicates from {list1}, {list2}, {list3}')

# Finding the duplicates between list 1 and 2, 1 and 3, 2 and 3
duplicatesList1 = list(set(list1) & set(list2))
duplicatesList2 = list(set(list1) & set(list3))
duplicatesList3 = list(set(list2) & set(list3))

# Combine the duplicate lists with unique values
finalDuplicateList = list(set(duplicatesList1 + duplicatesList2 + duplicatesList3))

print(f'Duplicates are {finalDuplicateList}')

'''Question 7: Find the first non repeating element in a given list of integers.'''

# List with repeated and non repeated elements
givenList = [2, 4, 6, 7, 8, 11, 13, 15, 17, 19, 2, 4, 6, 11, 15]

# To store elements that are undergone for duplicate check
verifiedElement = []

# To store duplicate elements from the list
duplicateElement = []

for num in givenList:

    # Find and store the duplicated elements from the given list
    if num in verifiedElement and num not in duplicateElement:
        duplicateElement.append(num)

    # Store the elements that are underwent for duplicate verification
    else:
        verifiedElement.append(num)

# remove the duplicates from the given list
newList = list(set(givenList) - set(duplicateElement))

# get the first non repeated element from the list
print(f'Question7: The first non repeated element in the {givenList} is: {newList[0]}')

print("Question8: Find a minimum element in [100, 87, 201, 315, 5, 1000]")

givenList = [100, 87, 201, 315, 5, 1000]

# sort the given list
givenList.sort()

print(f'The minimum element in the list is: {givenList[0]}')

'''Question9: Find the triplet in [10,20,30,9] whose sum = 59'''

print("Question9: Find the triplet in [10,20,30,9] whose sum = 59")

givenList = [10, 20, 30, 9]
targetSum = 59

# Length of the list
givenListLength = len(givenList)

# Brute force approach using three nested loops
for i in range(givenListLength - 2):
    for j in range(i + 1, givenListLength - 1):
        for k in range(j + 1, givenListLength):
            if givenList[i] + givenList[j] + givenList[k] == targetSum:
                print("The Triplet is:", givenList[i], givenList[j], givenList[k])
                break

'''Question10: [4,2,-3,1,6] Find if there is a sublist with sum = 0'''

print("Question10: [4,2,-3,1,6] Find if there is a sublist with sum = 0")

givenArray = [4, 2, -3, 1, 6]
noOfElements = len(givenArray)

isSubSetFound = False

# Iterate all subset representations from 1 to 2^noOfElements - 1
for i in range(1, 2 ** noOfElements):
    subset_sum = 0
    subset = []

    k = i  # Copy of i for bit checking
    index = 0

    while k > 0:
        if k % 2 == 1:  # If the lowest bit is 1, include arr[index]
            subset_sum += givenArray[index]
            subset.append(givenArray[index])
        k = k // 2  # Move to the next bit
        index += 1

    # Calculate the sum of subset, and print the subset if the sum is 0
    if subset_sum == 0:
        print("Subset with sum 0 is:", subset)
        isSubSetFound = True
        break

if not isSubSetFound:
    print("No subset with sum 0 found.")
