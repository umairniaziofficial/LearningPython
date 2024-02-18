import random


def coin_flip_simulation(num_flips):

    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):

        outcome = random.choice(["Heads", "Tails"])

        if outcome == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    print(f"Number of flips: {num_flips}")
    print(f"Heads: {heads_count}")
    print(f"Tails: {tails_count}")


num_flips = int(input("Enter the number of coin flips: "))


coin_flip_simulation(num_flips)
