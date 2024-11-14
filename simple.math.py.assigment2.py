def inc(n):
    return (1 + n)


def inc_with(n, t):
    return (n + t)


def greatest(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def power(x, n):
    return x**n


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


print('41 plus 1:', inc(41))

print('30 plus 12:', inc_with(30, 12))

print('Which is greater, 24 or 42?', greatest(24, 42))

print('Is 42 even?: ', is_even(42))

print('2 to the power of 10: ', power(2, 10))

print('Factorial of 5:', factorial(5))

print('Is 41 a prime?: ', is_prime(41))
