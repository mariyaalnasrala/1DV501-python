import list_functions as lf

# n antal slumpmässiga tal mellan 1 och 100

lst = (lf.random_list(10))
print(lst)

# medelvärdet av siffror i listan

lsta = [150, 60, 34, 22, 36]
print('Avrage of numbers in the list: ', end='')
print(lf.average_lst(lsta))


# retunera endast udda tal i en lista

numbers = [1, 2, 3, 4, 5, 6, 7]
result = lf.only_odd(numbers)
print(result)


# retunera en kommaavgränsad strängrepresentation

print(lf.to_string([1, 2, 3]))
print(lf.to_string(["a", "b", "c"]))


#  returnerar Sant om a följs direkt av b någonstans i listan lst.

print(lf.contains([1, 2, 3, 4], 3, 4))
print(lf.contains([5, 4, 6, 8], 4, 8))


# retunera true om listan innehåller dubbletter

print(lf.has_duplicates(['Hello', 'you', 'and', 'you']))
