import os


def isPrime(num):
    if num < 2:
        return False
    divisor = 2
    while divisor <= (num**0.5):
        if num % divisor == 0:
            return False
        divisor += 1
    return True


def nextPrime(abc):
    abc += 1
    while not isPrime(abc):
        abc += 1
    return abc


loopBool = True
number = 1

while loopBool:
    choice = int(input("[1] Next\n[2] Exit\n"))
    if choice == 1:
        number = nextPrime(number)
        os.system("cls")
        print(number)
    elif choice == 2:
        print("Exiting Program")
        loopBool = False
    else:
        print("Invalid choice. Please enter 1 or 2.")
