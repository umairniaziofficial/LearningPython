def binary_to_decimal(num):
    lastDigit = 0
    sum = 0
    i = 0
    while num != 0:
        lastDigit = num % 10
        num = num // 10
        sum = sum + lastDigit * (2**i)
        i = i + 1
    return sum


def decimal_to_binary(num):
    Binary = ""
    if num == 0:
        return "0"

    while num != 0:
        remainder = num % 2
        Binary = str(remainder) + Binary
        num = num // 2

    return Binary


if __name__ == "__main__":
    loop_bool = True

    while loop_bool:
        number = input("Enter Number: ")

        try:
            number = int(number)
        except ValueError:
            print("Invalid Input! Please enter a valid integer.")
            continue

        choice = int(
            input(
                "[*] Convert \n[1] Binary to Decimal\n[2] Decimal to Binary\n[3] Exit\n"
            )
        )

        if choice == 1:
            ans = binary_to_decimal(number)
            print(f"Decimal equivalent: {ans}")
        elif choice == 2:
            ans = decimal_to_binary(number)
            print(f"Binary equivalent: {ans}")
        elif choice == 3:
            print("Thanks For Using Our Application!")
            print("Exiting...")
            loop_bool = False
        else:
            print("Invalid Input!")
