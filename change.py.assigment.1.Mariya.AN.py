# Läs in priset från tagnetbordet
price = float(input('Price:'))

# Läs in betalning från tagnetbordet
payment = float(input('Payment:'))

# Räkna beloppet som är kvar
change = int(payment - price)

# Skriv ut belopp
print('Change:', change, 'kr')

# Beräkna hur många tusenlappar finns kvar i beloppet
bills1000 = change // 1000
print('1000 kr bills: ', bills1000)

# kvar belopp efter tusenlapp

restchange = change % 1000
# print(restchange)

# Beräkna hur många 500lappar finns kvar i beloppet

bills500 = restchange // 500
print('500kr bills: ', bills500)

# Kvarbelopp efter 500lappar

restch = restchange % 500
# print(restch)

# Beräkna antal 200lappar i beloppet

bills200 = restch // 200
print('200kr bills: ', bills200)

# Kvarbelopp efter 200lapp
restch1 = restch % 200
# print(restch1)

# Beräkna antal 100lappar i beloppet
bills100 = restch1 // 100
print('100kr bills: ', bills100)

# Kvarbelopp efter 100lappar
restch2 = restch1 % 100
# print(restch2)

# Beräkna antal 50lappar i beloppet
bills50 = restch2 // 50
print('50kr bills: ', bills50)

# Kvarbelopp efter 50lappar
restch3 = restch2 % 50
# print(restch3)

# Beräkna ntal 20lappar i beloppet
bills20 = restch3 // 20
print('20kr bills: ', bills20)

# Kvarbelopp efter 20lappar
restch4 = restch3 % 20
# print(restch4)

# Beräkna antal 10myntar i beloppet
bills10 = restch4 // 10
print('10kr coins: ', bills10)

# Kvarbelopp efter 10myntar
restch5 = restch4 % 10
# print(restch5)

# Beräkna antal 5mynt i beloppet
bills5 = restch5 // 5
print('5kr coins: ', bills5)

# Kvarbelopp efter 5myntar
restch6 = restch5 % 5
# print(restch6)

# Beräkna antal 2myntar i beloppet
bills2 = restch6 // 2
print('2kr coins: ', bills2)

# Kvarbelopp efter 2myntar
restch7 = restch6 % 2
# print(restch7)

# Beräkna antal 1mynt i beloppet
bills1 = restch7 // 1
print('1kr coins: ', bills1)
