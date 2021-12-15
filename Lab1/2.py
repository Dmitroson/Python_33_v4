import math

def get_digits(number):
    digits = []
    while(number > 0):
        digits.append(number % 10)
        number = number // 10
    return digits

n = int(input('N: '))
digits = get_digits(n)

s = sum(digits)
m = math.prod(digits)

print('S: ', s)
print('M: ', m)