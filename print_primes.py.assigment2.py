def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


# antal primtal
max_prime = int(input('How many primes? '))
count = 0
prim_count = 2

while prim_count <= max_prime + 1:
    if (isPrime(count)):
        print(count, end=' ')
        prim_count += 1
        count += 1
        if prim_count % 10 == 0:
            print()
    count += 1
