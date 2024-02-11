from collections import Counter

my_list = [1, 1, 1, 1, 2, 3, 3, 3, 2, 5, 2, 5, 1, 2, 7, 8, 8]

c = Counter(my_list)
a = c.most_common()

for key, value in a:
    print(f"{key} comes for {value} times")


# Operation 1
sum_of_values = sum(c.values())
print(f"\nSume of Values: {sum_of_values}")

# Operation 2
print("\nList: ", list(c))

# Operation 3
print("\nSet: ", set(c))

# Operation 4
print("\nDictiory: ", dict(c))

# Operation 5
print("\nItems: ", c.items())

# Operation 6
print("\nElement Pairs: ", Counter(dict(c)))

# Operation 7
print("\nMost Common Elements: ", c.most_common())

# Operation 8
print("\nLeast Common Elements: ", c.most_common()[::-1])
