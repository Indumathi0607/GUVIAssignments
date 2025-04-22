'''Question 1: Guess the number
This program is to guess the random number selected by the computer
'''

import random
from random import sample

print("Question 1: Guess the number")
# Store a random number
randomNumber = random.randint(0, 100)
# print(randomNumber)

# Get a number between 0 and 100 from user
userGuess = int(input("Enter a number between 0 and 100: "))

# When users input matches the random number
while 0 <= userGuess <= 100:
    if userGuess == randomNumber:
        print("Well done!!! your guess is correct")
        break

    # When the user input is lesser than the random number
    elif userGuess < randomNumber:
        if userGuess > randomNumber - 5:
            print("You're very close; your guess is lower than the random number.")
        else:
            print("Your guess is too low")

    # When the user input is greater than the random number
    elif userGuess > randomNumber:
        if userGuess < randomNumber + 5:
            print("You're very close; your guess is greater than the random number.")
        else:
            print("Your guess is too high")
    userGuess = int(input("Re-enter a number between 0 and 100: "))

else:
    print("Sorry!!! Number is no in range")

'''Question 2: Word Scramble
Unscramble a jumbled word from the below word list 
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']'''

print("Question 2: Word scramble")
wordList = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Fetch a word from the list randomly
randomWord = random.choice(wordList)
# print(randomWord)

# Scramble the word using join and sample methods
scrambledWord = ''.join(sample(randomWord, len(randomWord)))
print(scrambledWord)

userGuessWord = input("Guess the word: ")

while userGuessWord:
    if userGuessWord == randomWord:
        print("Well done!!!")
        break
    else:
        userGuessWord = input("sorry! wrong answer. Please retry: ")
else:
    print("No input given")
