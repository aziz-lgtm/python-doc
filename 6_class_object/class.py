# Creating a Class
# class ClassName:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sample_method(self):               
#         print(self.name.upper())

# class ClassName is made up of the class keyword to create a class, followed by the name of the class, here called ClassName. It is common in Python to use the PascalCase convention when naming classes.

# def __init__(self, name, age) is the special method automatically called when a new object is created. It initializes the attributes of the objects that will be created with the class.

# In addition to that, the first parameter of __init__ is always a reference to the specific object being created or used. By convention, this parameter is named self, but technically, you can use any name. self lets you access the object's own attributes and methods.

# self.name = name and self.age = age are the attributes the objects will have.

# def sample_method(self): is the method each object created can call.

# print(self.name.upper()) is what the sample_method method will do, in this case, it prints the name in uppercase.

# A Dog Class Example
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof!")

# Creating Objects from a Class
# With this Dog class, you can create an object. Here's the basic syntax for creating objects from a class:
# # object_1 = ClassName(attribute_1, attribute_2)
# object_2 = ClassName(attribute_1, attribute_2)
# You can also call any of the methods defined in the class from each object:
# object_1.method_name()
# object_2.method_name()

# Now let's create two dogs by using the Dog class as the blueprint:

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# Call the bark method
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!

# Differences between Classes and Objects
# In summary, the difference between a class and an object is that a class is the template or the blueprint, and an object is what is created using that template.
# Also, a class defines what data and behavior the object should have, and an object holds the actual data and uses that behavior. You write a class once, and you can make many objects from it, each with different data.
