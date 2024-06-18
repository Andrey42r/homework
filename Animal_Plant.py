class Animal:
    alive = True  #живой
    fed = False  #накормленный

    def __init__(self, name):
        self.name = name


class Plant:
    edidle = False  #съедобность

    def __init__(self, name):
        self.name = name


class Mammal(Animal):  #млекопитающие
    def eat(self, food):
        foo = Plant(Mammal)
        food = Mammal(Animal)
        if food != Plant.edidle:
            print("<self.name> съел <food.name>") and Animal.fed == True
        else:
            print("<self.name> не стал есть <food.name>") and Animal.alive == False


class Predator(Animal):  #хищники
    def eat(self, food):
        self.food = Plant(Predator)
        food = Predator(Animal)
        if food != Plant.edidle:
            print("<self.name> съел <food.name>") and Animal.fed == True
        else:
            print("<self.name> не стал есть <food.name>") and Animal.alive == False


class Flower(Plant):  #цветы
    pass


class Fruit(Plant):  #фрукты
    edidle = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
