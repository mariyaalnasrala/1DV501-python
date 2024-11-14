import random

num = random.randint(1, 100)
answer = 0
guess = 0
count = 0

while answer != num:

    guess += 1
    count += 1
    answer = int(input("Guess "))

    if count == 10:
        print('Try again later!')
        break

    elif answer < num:
        print('Clue: Higher')

    elif answer > num:
        print('Clue: Lower')

    elif answer == num:
        print('Correct answer after only', guess, 'guesses - Ecellent!')
