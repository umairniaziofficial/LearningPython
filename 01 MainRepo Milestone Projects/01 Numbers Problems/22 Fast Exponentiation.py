def FastExpo(base, expo):
    result = 1
    while expo > 0:
        if expo % 2 == 1:
            result = result * base
        base = base * base
        expo //= 2
    return result


base = int(input("Enter the Base: "))
expo = int(input("Enter the Expo: "))

ans = FastExpo(base, expo)
print(f"Value: {ans}")
