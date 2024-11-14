
# läs in kapital från tangetbordet
moneyc = int(input('Initial savings: '))

# läs in ränta från tangetbordet
interest = int(input('Interest rate (in percentages): '))

# läs in antal år från tangetbordet
years = int(input('Number of years: '))

# räckna värdet på sparande efter angivna år,
# sparkapital x (1+(räntan i procent/100)) ^ antal år
result = moneyc*(1+interest/100)**years

# skriv ut värdet i ett heltal korrekt avrundat
print('The value of your savings after ', years, 'years is: ',  round(result))
