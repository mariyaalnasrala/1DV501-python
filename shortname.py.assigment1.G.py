
firsrtn = str(input('First name: '))
middlen = str(input('Middle name: '))
lastn = str(input('Last name: '))

shortn = ((firsrtn[0] + '.') + (middlen[0] + '.') + lastn[0:4])
# (lastn[0]) + (lastn[1]) + (lastn[2]) + (lastn[3])) 
# short = lastn[0:3]
print(shortn)
