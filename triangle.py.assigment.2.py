# läs in nummer från tagentbordet
n = int(input('Enter an odd positive integer: '))

# för varje tal i nummeret skriv ut
for i in range(n):
    print(" " * i + "*" * (n - i))


# för varje tal i n skriv ut
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)

for i in range(1, n+1):
    space = ' '
    print('*' * i)
