def Fib(num):
    first = 0
    second = 1
    for i in range(num):
        print(first, end=" ")
        temp, first = first, second
        second = second + temp


Fib(100)
