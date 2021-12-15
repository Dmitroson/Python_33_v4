def power(n, p):
    if(p == 0):
        return 1
    
    return n * power(n, p - 1)

n = int(input("The number: "))
p = int(input("The power: "))

if(p > 0):
    print("Result: ", power(n, p))
else:
    p = abs(p)
    print("Result: ", 1 / power(n, p));