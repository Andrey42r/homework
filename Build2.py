class Building:
    total = 0

    def __init__(self, name):
        self.name = name
        Building.total += 1


Total = []
for i in range(1, 41):
    Tot = Building(i)
    Total.append(Tot)

for Tot in Total:
    print(Tot.name)
