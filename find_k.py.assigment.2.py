# läs in en siffra från tangetbordet
number = int(input('Enter a positive integer: '))

# Fel medellande om siffran är negativ
if number <= 0:
    print('Wrong input! write a positive integer!')

# start summan
sum = 1
# smallest k
k = 0

# så länge k är mindre än nummer addera
while k < number:
    k += sum
    sum = sum + 2

# Skriv ut resultat
print(f'{sum} is the smallest k such that 1+3+5+..+k > {number}')

# start summan
summa = 0

m = 0
# öka m med två så länge summan mindre än inm nummer
while summa < number:
    m += 2
    summa += m

# skriv ut resultat
print(f'{m-2} is the largest k such that 0+2+4+6+..+k <{number}')
