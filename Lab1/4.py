def generate_fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    return generate_fibonacci_sequence(n - 1) + generate_fibonacci_sequence(n - 2)

n = int(input('Enter the N-th number of Fibonacci sequence: '))

print('The N-th element of Fibonacci sequence: ', generate_fibonacci_sequence(n))