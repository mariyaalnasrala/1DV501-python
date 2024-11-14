import random

rand = random.randint(-10, 10)
print('The generated number is: ', rand)

randp = rand // 2

randn = rand % 2

if rand // 2 and rand > 0:
    print(str(randp) + ' is odd and positive ')
elif rand % 2 and rand < 0:
    print(str(randn) + ' is even and negative')
elif rand // 2 and rand < 0:
    print(str(randp) + ' is odd and negative')
elif rand % 2 and rand > 0:
    print(str(randn) + ' is even and positive')
