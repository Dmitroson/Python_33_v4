a = int(input('1st side: '))
b = int(input('2nd side: '))
c = int(input('3rt side: '))

isExisting = (a < b + c) and (b < a + c) and (c < a + b)

if isExisting:
    print('Yes')
else:
    print('No')