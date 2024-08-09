import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    name = 'name.txt'
    with open(name, 'r') as file:
        while True:
            first_line = file.readline()
            if not first_line:
                break
        all_data.append(first_line)


if __name__ == '__main__':
    filenames = [f'name.txt' for number in range(1, 5)]

#Линейный вызов
start_time = time.time()
for filename in filenames:
    read_info(filename)
print(f"Линейный вызов: {time.time() - start_time} секунд")


# Многопроцессный вызов
start_time = time.time()
with Pool(processes=4) as pool:
    pool.map(read_info, filenames)
print(f"Многопроцессный: {time.time() - start_time} секунд")