positive_numbers = []

count = 0

while True:
    number = int(input("Enter positive integers."))
    if number < 0:
        break
    elif number > 0:
        count += 1
        print(f'integer {count}: {number}')
        positive_numbers.append(number)
    else:
        print('Its negative number!')
print(f'Number of positive integers: {count}')
print(f'Positive numbers: {positive_numbers}')
