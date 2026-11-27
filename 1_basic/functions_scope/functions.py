# Functions are reusable pieces of code that run when you call them.

# input(), which lets you prompt the user for input:
name = input('What is your name?') # User types "Kolade" and presses Enter  
print('Hello', name) # Output: Hello Kolade

# int() converts a number, a boolean, or a string representing an integer into an integer:

print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0

# You can also write your own custom functions. To do that, you use the def keyword
def hello():
    print('Hello World')
    hello()
    # To run the function, you need to call it with its name followed by a pair of parentheses:


    # Using Parameters and Arguments
def calculate_sum(a, b):
    print(a + b)
    calculate_sum(3, 1) # 4

    # If you call the function without the correct number of arguments, you'll get a TypeError:

calculate_sum()
# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'

# Positional and Keyword Arguments
def introduce(name, age):
    print(f'My name is {name} and I am {age} years old.')

introduce('Alice', 25)
# My name is Alice and I am 25 years old.

# You can also pass keyword arguments by writing the parameter name followed by = and a value
introduce(age=25, name='Alice')
# My name is Alice and I am 25 years old.

# You can combine positional and keyword arguments, but the positional arguments must come first:
introduce('Alice', age=25)
# My name is Alice and I am 25 years old.

# You also cannot supply a value for the same parameter more than once:

introduce('Alice', name='Bob', age=25)
# TypeError: introduce() got multiple values for argument '

# Functions also use a special return keyword to exit the function and return a value. If you don't explicitly use return, Python will return None by default.

def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None

# You can see that the calculate_sum function prints the sum of a and b, but it doesn't return anything explicitly. So when we assign its result to my_sum, the value is actually None. To fix that, you can use the return keyword to send back the result:
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4