
# Yes, this is called polymorphism. Different objects respond differently to the same method call based on their class type. It is used to write flexible, reusable code and allows the same interface to represent different behaviors.

# Base Class

class Animal:
    """
    Base class representing an animal.
    """
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Animal Name: {self.name}")


# Mammal inherits Animal

class Mammal(Animal):
    """
    Mammal class inherits from Animal.
    """
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


# Bird inherits Animal

class Bird(Animal):
    """
    Bird class inherits from Animal.
    """
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


# Fish inherits Animal

class Fish(Animal):
    """
    Fish class inherits from Animal.
    """
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature

# Mammal children

class Dog(Mammal):
    def walk(self):
        print(f"{self.name} walks on four legs.")


class Cat(Mammal):
    def walk(self):
        print(f"{self.name} walks gracefully.")


# Bird children

class Eagle(Bird):
    def fly(self):
        print(f"{self.name} flies high in the sky.")


class Penguin(Bird):
    def swim(self):
        print(f"{self.name} swims instead of flying.")


# Fish children

class Salmon(Fish):
    def swim(self):
        print(f"{self.name} swims upstream.")


class Shark(Fish):
    def swim(self):
        print(f"{self.name} swims powerfully in the ocean.")



# Testing the classes

dog = Dog("Dog", "Warm-blooded")
cat = Cat("Cat", "Fur covered")

eagle = Eagle("Eagle", "Feathers")
penguin = Penguin("Penguin", "Cannot fly")

salmon = Salmon("Salmon", "Gills")
shark = Shark("Shark", "Sharp fins")

print("\n--- Mammals ---")
dog.show_name()
dog.walk()

cat.show_name()
cat.walk()

print("\n--- Birds ---")
eagle.show_name()
eagle.fly()

penguin.show_name()
penguin.swim()

print("\n--- Fish ---")
salmon.show_name()
salmon.swim()

shark.show_name()
shark.swim()
