'''
Polymorphism
Polymorphism is a programming concept that allows objects of different classes to be treated as objects of a common superclass. It is a key feature of object-oriented programming (OOP) and enables code reusability and flexibility.
'''
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Example of polymorphism
def animal_sound(animal):
    print(animal.speak())


# Create instances of Cat and Dog
cat = Cat()
dog = Dog()
# Call the animal_sound function with different animal objects
animal_sound(cat)  # Output: Meow!
animal_sound(dog)  # Output: Woof!
