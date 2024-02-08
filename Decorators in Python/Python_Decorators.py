def new_decorated_func(original_func):
    def wiii():
        print("Before decorating")
        original_func()
        print("After decorating")

    return wiii


@new_decorated_func
def F():
    print("F")


F()

# Hello = new_decorated_func(F)

# Hello()
