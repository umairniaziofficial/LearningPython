import random


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low + 1, high - 1)


for num in rand_num(1, 10, 12):
    print(num)

print(list(rand_num(1, 10, 12)))
