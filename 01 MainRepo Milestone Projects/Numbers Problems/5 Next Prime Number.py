def is_Prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def nextPrimeNumber(num):
    num += 1
    while not is_Prime(num):
        num += 1
    return num


if __name__ == "__main__":
    loopBool = True
    number = 1
    while loopBool:
        choice = int(input("[1] Next Prime number\n[2] Exit\n"))
        if choice == 1:
            number = nextPrimeNumber(number)
            print(f"{number} is the Next Prime Number.")
        elif choice == 2:
            loopBool = False
        else:
            print("Invalid Input")
