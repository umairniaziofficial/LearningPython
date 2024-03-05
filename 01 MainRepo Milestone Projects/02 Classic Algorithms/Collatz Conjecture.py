# Collatz Conjecture - Start with a number n > 7. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def Collatz(number):
    steps = 0
    while number > 1:
        if number%2==0:
            number = number//2
            steps+= 1
        else:
            number = number *3 + 1
            steps+= 1
    return steps


loopBool = True

while loopBool:
    number = int(input("Enter the Number: "))
    if number <= 7:
        print("The Value is Invalid! Please Enter a value Greater Than 7")
    else:
        Steps = Collatz(number)
        print(f"Total Steps Taken in Collatz Conjecture is {Steps}")
        loopBool = False
