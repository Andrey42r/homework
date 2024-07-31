from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово №{i}\n')
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = datetime.now()
print(f"Работа функций {end_time - time_start}")


time_start = datetime.now()
one_ = Thread(target=write_words, args=(10, "example5.txt"))
two_ = Thread(target=write_words, args=(30, "example6.txt"))
three_ = Thread(target=write_words, args=(200, "example7.txt"))
four_ = Thread(target=write_words, args=(100, "example8.txt"))

one_.start()
two_.start()
three_.start()
four_.start()

one_.join()
two_.join()
three_.join()
four_.join()

end_time = datetime.now()
print(f"Работа функций {end_time - time_start}")
