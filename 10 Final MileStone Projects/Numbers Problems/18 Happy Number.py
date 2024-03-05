def checkHappyNumber(x):
    while x >= 7:
        temp_sum = 0
        original_x = x
        while original_x > 0:
            r = original_x % 10
            temp_sum = temp_sum + (r**2)
            original_x = original_x // 10
        x = temp_sum
    return x == 1


def limitHappy(count):
    happyNo = []
    number = 1
    while len(happyNo) < count:
        if checkHappyNumber(number):
            happyNo.append(number)
        number = number + 1
    return happyNo


n = int(input("No of Happy Numbers you want: "))
ans = limitHappy(n)

print(ans)
