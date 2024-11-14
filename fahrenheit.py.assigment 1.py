# Be användaren att skriva temp i fahrenheit och läs den från tangetbordet
tempf = float(input("Provide a temperature in Fahrenheit: "))

# Räckna ut temp i C med hjälp av förhållandet mellan C och f.
c = (tempf-32) / 1.8

# skriv ut temp i celsius
print('Corresponding temperature in Celsius is:', c)

# Avrundat resultat
print('Corresponding temperature in Celsius is:', round(c))
