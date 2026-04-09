class Animal:
    def __init__(self, alive):
        self.alive = alive
    def speak(self):
        print("Animal makes a sound") 
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
class Car:
    def speak(self):
        print("Car honks")
animals = [Dog(True), Cat(True), Animal(True), Car()]
for animal in animals:
    animal.speak()