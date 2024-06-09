class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self):
        global i
        self.new_floor = int(input('Введите номер этажа: '))
        for i in range(1, self.new_floor):
            print(i)
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print('Такого этажа не существует')



dom = House("ЖК весна", 21)

print(dom.name, dom.number_of_floors)
dom.go_to()