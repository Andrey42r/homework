result = 0
incorrect_data = 0
len_ = 0

def personal_sum(numbers):
    global result, incorrect_data, len_
    try:
        for i in numbers:
            try:
                result += i
                len_ += 1
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
        return result, incorrect_data, len_
    except TypeError:
        return


def calculate_average(numbers):
    global result, incorrect_data, len_
    try:
        result, incorrect_data, len_ = personal_sum(numbers)
        try:
            average = result / len_
            return average
        except ZeroDivisionError:
            return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

