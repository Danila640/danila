class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Hero(Person):
    def __init__(self, name, age, superpower):
        super().__init__(name, age)
        self.superpower = superpower

hero = Hero("Superman", 30, "flight")
print(f"Hero: {hero.name}, Age: {hero.age}, Superpower: {hero.superpower}")