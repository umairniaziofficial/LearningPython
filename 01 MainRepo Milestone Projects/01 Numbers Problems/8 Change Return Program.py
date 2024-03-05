def UserInput():
    product_price = float(input("Enter the price of the Product: "))
    customer_given = float(input("Enter The price the Customer Given: "))
    return (product_price, customer_given)


def ChangePrice(a, b):
    return b - a


def CoinDistribution(change):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while change > 0:
        if change >= 25:
            change -= 25
            quarters += 1
        elif change >= 10:
            change -= 10
            dimes += 1
        elif change >= 5:
            change -= 5
            nickels += 1
        else:
            pennies = change
            change = 0

    return (quarters, dimes, nickels, pennies)


if __name__ == "__main__":
    value = UserInput()
    loopBool = True

    while loopBool:
        cost_price, price_given = value
        print(f"Product Price: {cost_price}")
        print(f"User Given: {price_given}")

        if cost_price < 0 or price_given < 0:
            print("Invalid Input!")
            value = UserInput()
        else:
            ans = ChangePrice(cost_price, price_given)
            if ans < 0:
                print(f"Please Give {ans*(-1)} More Money!")
                loopBool = False
            else:
                changeValue = CoinDistribution(ans)
                print(f"You have to give {ans} Change to The Customer")
                q, d, n, p = changeValue
                print(f"{q} Quarters {d} Dimes {n} nickels and {p} pennies")
                loopBool = False
    print("[*] Thanks For Shopping!")
