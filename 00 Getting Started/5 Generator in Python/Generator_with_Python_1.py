# def Cubes_of_Numbers(n):
#     for i in range(n):
#         yield i**3


# for i in Cubes_of_Numbers(10):
#     print(i)

# lst = list(Cubes_of_Numbers(10))
# print(lst)


def gen_fibon(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for n in gen_fibon(10):
    print(n)
