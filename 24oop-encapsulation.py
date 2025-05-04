'''
Encapsulation example

__ represents private attributes
and methods in Python.
For eg:
    __name: means that name is a private attribute and is accessible only within the class.
'''
class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

# Example usage
person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30
person.set_age(35)
print(person.get_age())   # Output: 35
person.set_age(-5)  # Output: Age must be positive


#this line will raise an error
# print(person.__name) 