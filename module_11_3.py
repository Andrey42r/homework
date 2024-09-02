import inspect

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


def introspection_info(obj):
    _type = type(obj)
    _dir = obj.__dict__
    _method = dir(obj)
    _module = inspect.getmodule(obj)
    print(f'type: {_type}, attributes: {_dir}, methods: {_method}, module: {_module}')


number_info = introspection_info(dom)
print(number_info)
