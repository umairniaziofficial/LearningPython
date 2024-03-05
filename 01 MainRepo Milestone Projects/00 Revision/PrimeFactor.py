def isPrime(num):
    if num == 1 or num == 0:
        return False
    divisor = 2
    while divisor < (num**0.5):
        if num % divisor == 0:
            return False
        divisor = divisor + 1
    return True


print(isPrime(8))
