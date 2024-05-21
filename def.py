#Функция с параметрами по умолчанию____________________________________________________________________________________

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1)
print_params(1, 2)
print_params(1, 2, 3)
print_params(b=25)
print_params(c=[1, 2, 3])

#Распаковка параметров_________________________________________________________________________________________________

def print_params(a, b, c):
    print(a, b, c)


values_list = [3, 'автобус', False]
values_dict = {'a': 4, 'b': 'телефон', 'c': [1, 3, 5]}

print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры______________________________________________________________________________________

def print_params(a, b, c):
    print(a, b, c)


values_list_2 = [78, 'Игнат']
print_params(*values_list_2, 42)
