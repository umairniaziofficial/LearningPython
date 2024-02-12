#  Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.


def find_area(length, width):
    return length * width


def calculate_cost(area, tile_cost):
    return area * tile_cost


def main():
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    cost = float(input("Enter the Cost of One Tile in Dollar: "))

    area = find_area(length, width)
    tile_cost = calculate_cost(area, cost)

    print(f"Total Area is: {area} square units")
    print(f"Total Price: ${tile_cost:.2f}")


if __name__ == "__main__":
    main()
