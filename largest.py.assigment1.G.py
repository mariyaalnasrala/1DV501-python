
print('Please provide three integers A, B, C.')
numberA = int(input('Entre A: '))
numberB = int(input('Enter B:'))
numberC = int(input('Enter C:'))
if numberA > numberB and numberA > numberC:
    print('The largest number is: ', numberA)
elif numberB > numberA and numberB > numberC:
    print('The largest number is: ', numberB)
elif numberC > numberA and numberC > numberB:
    print('The largest number is: ', numberC)
