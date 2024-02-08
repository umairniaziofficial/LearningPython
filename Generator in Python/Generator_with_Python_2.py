def multipleOfTwo(n):

    for i in range(1, n):
        yield i**2


ans = iter(multipleOfTwo(3))


print(next(ans))
print(next(ans))
