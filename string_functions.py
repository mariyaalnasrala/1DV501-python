
# funktionssammanslagning
def samman_lagning(text, num):
    result = text * num
    return result


# returenera antal x
def antal_tecken(s, x):
    sum = 0
    for letter in s:
        if letter == x:
            sum += 1
    return sum


# omvänd funktion
def reverse(s):
    res = (s)[::-1]
    return res


# första och sista tecken
def first_last(s):
    first = (s)[0]
    last = (s)[len(s)-1]
    return first, last


# retunera true om strängar innehåller x
def has_two_x(txt):
    count = 0
    for letter in txt:
        if letter == 'x':
            count += 1
            if count >= 2:
                return True
    return False


# innehåller dubbeltecken
def has_duplicates(s):
    let = set()
    for letter in s:
        if letter in let:
            return True
        let.add(letter)
    return False
