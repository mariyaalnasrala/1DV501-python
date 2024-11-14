import random
# n antal slumpmässiga tal mellan 1 och 100


def random_list(n):
    numbers = [random.randint(1, 100) for _ in range(n)]
    return numbers


# medelvärdet av siffror i listan

def average_lst(lst):
    total = sum(lst)
    num = len(lst)
    average = round(total / num)
    return average


# retunera endast udda tal i en lista

def only_odd(lst):
    odd_numbers = []
    for x in lst:
        if x % 2 != 0:
            odd_numbers.append(x)
    return odd_numbers


# retunera en kommaavgränsad strängrepresentation
def to_string(lst):
    s = ''
    for i in range(len(lst)):
        s += str(lst[i])

        if i < len(lst) - 1:
            s += ','
    return "[" + s + "]"


#  returnerar Sant om a följs direkt av b någonstans i listan lst.
def contains(lst, a, b):
    for i in range(len(lst) - 1):
        if lst[i] == a and lst[i + 1] == b:

            return True
    return False


# retunera true om listan innehåller dubbletter
def has_duplicates(lst):
    seen = set()
    for x in lst:
        if x in seen:
            return True
        seen.add(x)
    return False
