def find_fibonacci(to_limit):
    first = 0
    second = 1
    for i in range(to_limit):
        print(first)
        temp, first = first, second
        second = temp + second


if __name__ == "__main__":
    print("---Fibonacci Series---")
    limit_number = int(input("Enter the Limit of The Fibonacci You want: "))
    find_fibonacci(limit_number)
