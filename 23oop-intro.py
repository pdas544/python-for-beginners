'''
Introduction to Object-Oriented Programming (OOP) in Python
- It uses classes and objects to structure code
- Classes are blueprints for creating objects
- Objects are instances of classes
- It has following characteristics:
1. Encapsulation: Bundling data and methods that operate on the data within one unit (class).
2. Abstraction: Hiding complex implementation details and showing only the essential features of the object.
3. Inheritance: Mechanism to create a new class using properties and methods of an existing class.
4. Polymorphism: Ability to present the same interface for different data types.
'''
# Example of a simple class
class Dog:
    # Class attribute
    species = "Canis familiaris"  # Class attribute

    # Initializer / Constructor
    # This method is called when an object is created from the class
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an object (instance) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
# Accessing attributes and methods
print(dog1.description())  # Output: Buddy is 3 years old.
print(dog2.description())  # Output: Max is 5 years old.
print(dog1.speak("Woof"))  # Output: Buddy says Woof
print(dog2.speak("Bark"))  # Output: Max says Bark
# Accessing class attribute
print(f"{dog1.name} is a {dog1.species}")  # Output: Buddy is a Canis familiaris
# Accessing class attribute using the class name
print(f"{dog2.name} is a {Dog.species}")  # Output: Max is a Canis familiaris