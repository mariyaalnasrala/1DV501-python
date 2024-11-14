# Läs in antal sekonder från tagnetbordet
sec = int(input('Give a number of seconds: '))

# Räckna ut antal timmar från inmatade siffran
hours = sec // 3600
print(hours)

# Räckna ut resten av sekonder efter timar
restseconds = sec % 3600
# print(restseconds)

# Räckna antal minuter från resten av sekonder
minutes = restseconds // 60
print(minutes)

# Räkna antal sekonder från resten av minuter
second = restseconds % 60
print(second)

print('This corresponds to:', (hours), 'hours,', (minutes), ' minutes and', (second), 'seconds')
