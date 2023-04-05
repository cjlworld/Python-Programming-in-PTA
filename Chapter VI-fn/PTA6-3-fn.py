def CountDigit(number, digit):
    if number < 0:
        number = -number
    cnt = 0
    while number > 0:
        if number%10 == digit:
            cnt += 1
        number //= 10
    return cnt

# 注意整除是 //