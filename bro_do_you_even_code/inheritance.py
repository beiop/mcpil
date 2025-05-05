class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    pass
dog = Dog("Scooby")
print(dog.name)