# Write a lambda function to check if a given string is a number?

userInput = input("Give your input: ")

# Lambda expression to find a given positive, negative and float numbers
isNumber = lambda num: num.replace(".", "").replace("-", "").isnumeric()

print(f"{userInput} is number?: {isNumber(userInput)}")
