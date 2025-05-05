'''
Inheritance: 
- Inheritance is a way to form new classes using classes that have already been defined.
- The new class is called the derived class or child class, and the class from which it inherits is called the base class or parent class.
'''
class Animal:
    legs = 4  # Class variable
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Dog is a derived class of Animal
    def speak(self):
        return "Woof! Woof!"
    
class Cat(Animal):  # Cat is a derived class of Animal
    def speak(self):
        return "Meow!"

# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
# Calling the speak method of the derived classes
print(dog.speak())  # Output: Woof! Woof!
print(cat.speak())  # Output: Meow!
# Accessing the class variable from the base class
print(dog.legs)  # Output: 4
print(cat.legs)  # Output: 4