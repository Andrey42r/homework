import io
from pprint import pprint


def custom_write(file_name, strings, file=None, strings_positions=None):
    string_positions = {}
    strings = []
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in strings:
            start_position = file.tell()
            file.write(i + '/n')
            strings_positions = {(len(string_positions) + 1, start_position): i}
    return strings_positions


strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('file_name.txt', strings)
for elem in result.items():
    print(elem)
