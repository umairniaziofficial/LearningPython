import math
import os

os.system("cls")


def convert_to_monthly_interest_rate(annual_interest, compounding_interval):
    if compounding_interval == "monthly":
        return annual_interest / 12 / 100
    elif compounding_interval == "weekly":
        return annual_interest / 52 / 100
    elif compounding_interval == "daily":
        return annual_interest / 365 / 100
    elif compounding_interval == "continually":
        return annual_interest / 100
    else:
        print("Invalid compounding interval. Using monthly as default.")
        return annual_interest / 12 / 100


def calculate_monthly_payment(principal, monthly_interest_rate, num_terms):
    monthly_payment = (principal * monthly_interest_rate) / (
        1 - math.pow(1 + monthly_interest_rate, -num_terms)
    )
    return monthly_payment


def calculate_total_payback_time(num_terms, compounding_interval):
    if compounding_interval == "continually":
        return "Cannot calculate total payback time for continually compounded interest"
    else:
        return num_terms if compounding_interval == "monthly" else num_terms * 12


def display_results(monthly_payment, total_payback_time):
    print(f"\nMonthly Mortgage Payment: ${monthly_payment:.2f}")
    print(f"Total Payback Time: {total_payback_time} months")


if __name__ == "__main__":
    principal = float(input("Enter the principal amount of the loan: "))
    annual_interest_rate = float(
        input("Enter the annual interest rate (as a percentage): ")
    )
    num_terms = int(input("Enter the number of terms (N): "))
    compounding_interval = input(
        "Enter the compounding interval (monthly, weekly, daily, continually): "
    )
    monthly_interest_rate = convert_to_monthly_interest_rate(
        annual_interest_rate, compounding_interval
    )
    if monthly_interest_rate is not None:
        monthly_payment = calculate_monthly_payment(
            principal, monthly_interest_rate, num_terms
        )
        total_payback_time = calculate_total_payback_time(
            num_terms, compounding_interval
        )
        display_results(monthly_payment, total_payback_time)
