class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House("Орбита", 28)
h2 = House("Эдельвейс", 36)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

