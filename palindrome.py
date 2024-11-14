
def is_palindrome(er):
    er = er.replace(" ", "")
    er = er.lower()
    reversed_er = er[::-1]
    if er == reversed_er:
        return True
    else:
        return False


print(is_palindrome('was it a rat I saw'))
print(is_palindrome('A nut for a jar of tuna'))
print(is_palindrome('Madam'))
print(is_palindrome('Ni talar bra latin'))
print(is_palindrome('Hello'))
