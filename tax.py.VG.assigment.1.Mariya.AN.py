# Läsa in inmatad summa (inkomst)
income = int(input("Please provide monthly income: "))

# Räkna skatt för inkomster mindre än 38000
if income < 38000:

    # Skriv ut skatt för inkomsten om den är under 38000
    print("Corresponding income tax: ", round(income*30/100))

# Räkna skatt för inkomster mellan 50000 och 38000
elif income > 38000 and income < 50000:

    # Skriv ut skatt för inkomsten om den är mella 50000 och 38000
    print("Corresponding income tax: ", round(income*30.87/100))

# Räkna skatt för inkomster större än 50000
elif income > 50000:

    # Skriv ut skatt för inkomsten om den är större än 5000
    print("Corresponding income tax: ", round(income*34.43/100))
