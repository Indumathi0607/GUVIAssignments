# Create a lambda method to generate a Fibonacci series upto n numbers.

userInput = int(input("Enter a number: "))

# lambda method to find the fibonacci value of given number using Formula: F(n)=F(n−1)+F(n−2)
fibonacciSeries = lambda num: num if num <= 1 else fibonacciSeries(num - 1) + fibonacciSeries(num - 2)

# Create a fibonacci series for n terms (userInput) using List comprehension
fibSeriesList = [fibonacciSeries(i) for i in range(userInput)]

print(f"Fibonacci series for upto {userInput} is : {fibSeriesList}")
