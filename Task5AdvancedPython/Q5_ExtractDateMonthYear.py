'''Use a lambda function to extract the year, month and date from a datetime object'''

# Importing datetime object
from datetime import datetime

userInput = input("Enter a date in dd-mm-yyyy format: ")

# Use inbuilt datetime methods to convert user input into datetime
convertInputIntoDate = datetime.strptime(userInput, "%d-%m-%Y")

# lambda expression to assign year, date, month
extractYearMonthDate = lambda date: (f'Year: {date.year}, Month: {date.month}, Day: {date.day}')

print(f'Extracted values: {extractYearMonthDate(convertInputIntoDate)}')
