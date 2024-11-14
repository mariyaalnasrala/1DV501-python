import random

# läs in antal slump nummer som ska skrivas ut
num = int(input('Enter number of integers to be generated: '))

# fel medellande om nummer är negativ
if num <= 0:
    print('Please enter a positive integer!')

sum = 0
min_value = 100
max_value = 0

# skriv ut random nummer
print('Generated values:', end=' ')

for i in range(num):
    nummer = random.randint(1, 100)
    # öka summan för avrunding sen
    sum += nummer
    min_value = min(min_value, nummer)
    max_value = max(max_value, nummer)
    print(nummer, end=' ')

average = sum / num
print('\nAvrage', average)
print('min', min_value)
print('max ', max_value)
