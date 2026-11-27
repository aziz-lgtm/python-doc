# Here is the basic syntax for a list:
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0])

# negative indexing
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[-1])

# Using the list() Constructor

developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']
print(list(developer))

# Getting the Length of a List
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # 5

# Updating List Elements
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

# IndexError
# programming_languages = ['Python', 'Java', 'C++', 'Rust']
# programming_languages[10] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""

# Removing Elements from a List
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']

# Checking If an Element Is in a List

programming_languages = ['Python', 'Java', 'C++', 'Rust']

print('Rust' in programming_languages)
print('Codex' in programming_languages)

# Working with Nested Lists
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2])
print(developer[2][1])#Rust

# Unpacking Values from a List
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

# *rest
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

# ValueError
# developer = ['Alice', 34, 'Rust Developer']
# name, age, job, city = developer

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
"""

# Slicing Lists
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:5]) # ['Cookies', 'Ice Cream', 'Pie']

# If you wanted to extract a list of just even numbers, you can use the slicing operator like this:
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1::2]) # [2, 4, 6]