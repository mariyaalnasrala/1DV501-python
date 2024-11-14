# läs en positive siffra från tagnetbordet
num = int(input("Enter a positive integer: "))
# skriv odda nummer mellan 1 och inmatade siffran
print('Odd numbers using for: ', end=" ")
for i in range(1, num, 2):
    # skriv ut resultat
    print(i, end=" ")
# första nummer i loopen ska börja med 1
n = 1
# alla nummer frn 1 till inmatade siffran
print('\nOdd numbers using while: ', end=" ")
while n <= num:
    # skriv ut resultat
    print(n, end=" ")
# addera 2 till siffran för att få de odda talen
    n += 2
print()
