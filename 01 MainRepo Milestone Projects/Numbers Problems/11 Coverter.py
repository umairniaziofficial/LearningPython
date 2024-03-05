def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")
    else:
        print("Invalid input. Please enter 1 or 2.")


def currency_converter():
    print("Currency Converter")
    print("1. USD to PKR")
    print("2. PKR to USD")

    exchange_rate_usd_to_pkr = 272

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        usd = float(input("Enter amount in USD: "))
        pkr = usd * exchange_rate_usd_to_pkr
        print(f"{usd} USD is equal to {pkr:.2f} PKR")
    elif choice == "2":
        pkr = float(input("Enter amount in PKR: "))
        usd = pkr / exchange_rate_usd_to_pkr
        print(f"{pkr} PKR is equal to {usd:.2f} USD")
    else:
        print("Invalid input. Please enter 1 or 2.")


def volume_converter():
    print("Volume Converter")
    print("1. Liters to Gallons")
    print("2. Gallons to Liters")

    choice = input("Enter choice (1 or 2): ")

    liters_to_gallons_conversion = 0.264172

    if choice == "1":
        liters = float(input("Enter volume in Liters: "))
        gallons = liters * liters_to_gallons_conversion
        print(f"{liters} Liters is equal to {gallons:.2f} Gallons")
    elif choice == "2":
        gallons = float(input("Enter volume in Gallons: "))
        liters = gallons / liters_to_gallons_conversion
        print(f"{gallons} Gallons is equal to {liters:.2f} Liters")
    else:
        print("Invalid input. Please enter 1 or 2.")


def mass_converter():
    print("Mass Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")

    choice = input("Enter choice (1 or 2): ")

    kilograms_to_pounds_conversion = 2.20462

    if choice == "1":
        kilograms = float(input("Enter mass in Kilograms: "))
        pounds = kilograms * kilograms_to_pounds_conversion
        print(f"{kilograms} Kilograms is equal to {pounds:.2f} Pounds")
    elif choice == "2":
        pounds = float(input("Enter mass in Pounds: "))
        kilograms = pounds / kilograms_to_pounds_conversion
        print(f"{pounds} Pounds is equal to {kilograms:.2f} Kilograms")
    else:
        print("Invalid input. Please enter 1 or 2.")


def unit_converter():
    print("Unit Converter")
    print("Choose the type of unit conversion:")
    print("1. Temperature")
    print("2. Currency")
    print("3. Volume")
    print("4. Mass")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        temperature_converter()
    elif choice == "2":
        currency_converter()
    elif choice == "3":
        volume_converter()
    elif choice == "4":
        mass_converter()
    else:
        print("Invalid input. Please enter a number between 1 and 4.")


unit_converter()
