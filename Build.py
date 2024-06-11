class Building:
    def __init__(self, int_, str_):
        self.numberOfFloors = int_
        self.buildingType = str_

    def __eq__(self, other):
        return self.numberOfFloors == self.buildingType


test = Building(1, 'test')
print(test.buildingType, test.numberOfFloors)
print(test.buildingType == test.numberOfFloors)