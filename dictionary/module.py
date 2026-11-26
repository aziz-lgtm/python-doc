# Let's say that you want to import the math module. In that case, you would write this at the top of your file:
import math

# Then, if you need to call a function from that module in your Python script, you would use dot notation, with the name of the module followed by the name of the function:
print(math.sqrt(36))

# If you need to import the module with a different name (also known as an "alias"), you can use this syntax, with as followed by the alias at the end of the import statement:
import math as m
# Then, you can access the elements of the module using the alias:
print(m.sqrt(36))

# Different Ways to Import Module Elements. But sometimes you don't need to import everything from a module. Perhaps you only need one or two specific functions or classes. Python has exactly what you need in that case.

# Now the import statement starts with from, followed by the name of the module, and then the import keyword followed by the name of the elements that you want to import:
# from module_name import name1, name2

from math import name1, name2

# Then, you can use these names without the module prefix in your Python script.

# If you want to assign aliases to these names, you can do that by using the as keyword after each, followed by the alias you want to use:
from math import name1 as alias1, name2 as alias2

# Let's say that you only want to import the radians, sine, and cosine functions from the math module. You would write:

from math import radians, sin, cos

# Now you can call these functions directly in your code, without the math module as a prefix.

# To find the sine and cosine of a specific angle initially expressed in degrees, we can call the radians function to convert it to radians, and then call the sine and cosine functions, passing the angle in radians:

from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978

# And finally, we find this import statement that ends with an asterisk. The asterisk is telling Python that you want to import everything that the module makes public, but you want to import it so that you don't need to use the name of the module as a prefix:
# from module_name import *

# For example, if you do this while importing the math module, you'll be able to call any function defined in that module without specifying the name of the module as a prefix. Here are some examples:
from math import *
print(sqrt(36))  # 6.0
print(pow(5, 2)) # 25.0
print(exp(1))    # 2.718281828459045

# However, this is generally discouraged because it can lead to namespace collisions, and make it harder to know where certain names are coming from.

# mport statements work exactly the same for functions, classes, constants, variables, and any other elements defined in the module.

# Here is an example of a constant from the math module, the number pi:
import math
print(math.pi)

# And here is an example of a class from the datetime module. We create a date object that represents July 15, 1959. Then, we assign that date object to a variable and access the day, month, and year individually using dot notation:
import datetime
birthday = datetime.date(1959, 7, 15)
print(birthday.day)    # 15
print(birthday.month)  # 7
print(birthday.year)   # 1959

# The if __name__ == '__main__' Idiom
# if __name__ == '__main__':

# This is why you'll often find this conditional in Python scripts. It contains the code that you want to run only if the Python script is running as the main program:
# But if the script is imported as a module, the code within that block doesn't run.
