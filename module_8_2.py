from self import self
result = 0
incorrent_data = 0
def personal_sum(numbers):
    global result, incorrent_data
    self.number = numbers
    while numbers != 0:
        result += numbers
    if numbers != int:
        incorrent_data += 1
        return result, incorrent_data
    
    try:
        total = personal_sum()
        print(total)
        
    except TypeError:
        print(f'В numbers записан некорректный тип данных')


def calculate_average(numbers):
    self.numbers = numbers

    try:
        total = calculate_average()
        print(total)
        sum(personal_sum())

    except ZeroDivisionError:
        print('0')

    except TypeError:
        print(f'Некорректный тип данных для подсчёта суммы {incorrent_data}')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать