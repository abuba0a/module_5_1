class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        number_of_floors = int(self.number_of_floors)

        if int(new_floor) > number_of_floors or int(new_floor) < 1:
            print('Такого этажа не существует')
        else:
            floor = 0
            for floor in range(0, new_floor):
                floor = floor + 1
                print(floor)
            return floor


H1 = House('ЖК Эльбрус', 30)
H2 = House('ЖК Горский', 18)
H3 = House('Домик в деревне', 2)
print(H1.name, H1.number_of_floors)
H1.go_to(0)
print()
print(H2.name, H2.number_of_floors)
H2.go_to(10)
print()
print(H3.name, H3.number_of_floors)
H3.go_to(3)