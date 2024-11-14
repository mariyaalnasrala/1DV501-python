# läs in en heltal siffra av 3 delar från tagnetbordet.
number = int(input('Provide a three digit number: '))

# Dela upp siffran till 3 delar
# första siffran (hundratal)
number1 = number // 100
# print(number1)

# mellan siffran (Tiotal)
number2 = number // 10
number2 = number2 % 10
# print(number2)

# sista siffran (ental)
number3 = number % 10
# print(number3)

# räkna och skriv ut summan av 3 siffror
sum = number1 + number2 + number3
print(sum)

# simple program
# number = int(input('Provide a three digit number: '))
# number1 = number // 100
# number2 = (number // 10) % 10
# number3 = number % 10
# sum = number1 + number2 + number3
# print(sum)
