def calculate_tax(cost, tax_rate):
    tax = cost * (tax_rate / 100)
    total_cost = cost + tax
    return tax, total_cost


def main():
    try:
        cost = float(input("Enter the cost: $"))
        tax_rate = float(input("Enter the tax rate (in percentage): "))

        tax, total_cost = calculate_tax(cost, tax_rate)

        print(f"\nTax: ${tax:.2f}")
        print(f"Total cost with tax: ${total_cost:.2f}")

    except ValueError:
        print("Please enter valid numeric values for cost and tax rate.")


if __name__ == "__main__":
    main()
