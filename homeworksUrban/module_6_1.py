class animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def __str__(self):
        return f"{self.name} (Живой: {self.alive}, Накормленный: {self.fed})"



class plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

    def __str__(self):
        return f"{self.name} (Съедобное: {self.edible})"


class mammal(animal):
    def eat(self, food):
        if isinstance(food,plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может съесть {food.name}, потому что это не растение")


class predator(animal):
    def eat(self, food):
        if isinstance(food, plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} cъел {food.name}, потому что он хищник и может себе позволить")

class flower(plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False


class fruit(plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = predator('лев')
a2 = mammal('капибара')
p1 = flower('герань')
p2 = fruit('яблоко')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a1.eat(a2)
a2.eat(a1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

