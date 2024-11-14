import random

lst = list(range(1, 36))

lottosekvens = random.sample(lst, 7)

lottosekvens.sort()
print('The lotto numbers this week:')
print(lottosekvens)
