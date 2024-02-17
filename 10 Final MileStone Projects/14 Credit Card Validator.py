def CleanCardNumber(cardNo):
    cardNumber = "".join(char for char in cardNo if char.isdigit())
    return cardNumber


def ValidateCardNumber(nocard):
    card_list = [int(digit) for digit in nocard[::-1]]
    for i in range(1, len(card_list), 2):
        card_list[i] *= 2
        if card_list[i] > 9:
            card_list[i] -= 9

    totalSum = sum(card_list)
    if totalSum % 10 == 0:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    userInput = input("Enter the Card No: \n")
    cardInput = CleanCardNumber(userInput)
    CardNumberValidate = ValidateCardNumber(cardInput)
    print(f"Card no {cardInput} is {CardNumberValidate}")
