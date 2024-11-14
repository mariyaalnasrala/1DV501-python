# Läs in namn på rutan från tagnetbrdet
chose = input("Enter a chess square identifier (e.g. e5): ")

# skapa en sträng för vita ruter
white = 'a8, a6, a4, a2, b7, b5, b3, b1, c8, c6, c4, c2, d7, d5, d3, d1'
white1 = 'e8, e6, e4, e2,f7, f5, f3, f1, g8, g6, g4, g2, h7, h5, h3, h1'

# skapa en sträng för svarta ruter
black = 'a7, a5, a3, a1, b8, b6, b4, b2, c7, c5, c3, c1, d8, d6, d4, d2'
black1 = 'e7, e5, e3, e1, f8, f6, f4, f2, g7, g5, g3, g1, h8, h6, h4, h2'

# skriv ut färgen på inmatade rutan
if chose in white or chose in white1:
    print(chose, "is white")
# skriv ut färgen på inmatade rutan
elif chose in black or chose in black1:
    print(chose, "is black")
