import random
# skapa en lista

lst = [0] * 11

# Simulera att rulla två tärningar
for _ in range(10000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    lst[total - 2] += 1

print('Frequency table (sum, count) for rolling two dices 10000 times')
for i in range(2, 13):
    print(f'Summa {i}: {lst[i - 2]} gånger')
