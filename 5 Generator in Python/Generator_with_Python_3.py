def genSquares(n):
    for i in range(n):
        yield i**2


for x in genSquares(10):
    print(x)
