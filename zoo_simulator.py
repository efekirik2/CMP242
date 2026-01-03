# Too many bugs in your code!!!

class Animal:
    def __init__(self, name, age, round):
        self.name = name
        self.age = age
        self.round = round

    def make_noise(self):
        print(f"{self.name} making noise...")

    def feed(self):
        print(f"{self.isim} feeding.")

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Type: {self.round}")

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Aslan")

    def make_noise(self):
        print(f"{self.name}: Roooaaarr!")

    def feed(self):
        print(f"{self.name} feeding with meat.")


class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Fil")

    def make_noise(self):
        print(f"{self.name}: Vuuuuuu!")

    def feed(self):
        print(f"{self.name} feeding with grass and leafs")


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Bird")

    def make_noise(self):
        print(f"{self.name}: Cik cik!")

    def feed(self):
        print(f"{self.name} feeding with seeds.")

class ZooPark:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} add to zoo park")

    def show_animals(self):
        print("\n Animals in the zoo park:")
        for h in self.animals:
            h.show_info()

    def daily_activities(self):
        print("\nDay begin! Daily activities of animals:")
        for h in self.animals:
            h.make_noise()
            h.feed()

if __name__ == "__main__":
    zoo =ZooPark()

    lion = Lion("Simba", 5)
    Elephant = Elephant("Dumbo", 10)
    bird = Bird("Tweety", 2)

    zoo.add_animal(lion)
    zoo.add_animal(Elephant)
    zoo.add_animal(bird)

    zoo.show_animals()
    zoo.daily_activities()

