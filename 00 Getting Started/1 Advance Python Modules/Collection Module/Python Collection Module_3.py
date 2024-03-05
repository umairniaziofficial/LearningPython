from collections import namedtuple

Dog = namedtuple("Dog", ["Age", "breed", "name"])

sammy = Dog("10", "German", "Tommy")

print(sammy[0])

print(sammy.Age)

print(sammy[1])
print(sammy.breed)
