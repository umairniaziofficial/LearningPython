def num_to_words(n):
    if n == 0:
        return "zero"
    elif n < 0:
        return "Negative " + num_to_words(-n)
    elif n <= 20:
        return [
            "",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ][n]
    elif n <= 99:
        return [
            "",
            "",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
        ][n // 10] + (" " + num_to_words(n % 10) if n % 10 != 0 else "")
    elif n <= 999:
        return (
            num_to_words(n // 100)
            + " hundred"
            + (" and " + num_to_words(n % 100) if n % 100 != 0 else "")
        )
    elif n <= 99999:
        return (
            num_to_words(n // 1000)
            + " thousand"
            + (" " + num_to_words(n % 1000) if n % 1000 != 0 else "")
        )
    elif n <= 9999999:
        return (
            num_to_words(n // 100000)
            + " lakh"
            + (" " + num_to_words(n % 100000) if n % 100000 != 0 else "")
        )
    elif n <= 99999999:
        return (
            num_to_words(n // 10000000)
            + " crore"
            + (" " + num_to_words(n % 10000000) if n % 10000000 != 0 else "")
        )


num = int(input("Enter the Number: \n"))
numberinWords = num_to_words(num)

print(f"Number: {num}\nWords: {numberinWords}\n")
