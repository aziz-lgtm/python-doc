# The commas create the tuple, so parentheses are optional in an assignment like this
developer = 'Alice', 34, 'Rust Developer'
print(developer) # ('Alice', 34, 'Rust Developer')

# To create a tuple with one element, you need a trailing comma:

single_value = (5,)
print(single_value) # (5,)

not_a_tuple = (5)
print(not_a_tuple) # 5
# An empty tuple is written as ().

# # If you try to update one of the items in the tuple, you will get a TypeError, tuples are immutable:
# programming_languages = ('Python', 'Java', 'C++', 'Rust')
# programming_languages[0] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""
# Accessing Tuple Elements
developer = ('Alice', 34, 'Rust Developer')
print(developer[1]) # 34

# from the last
numbers = (1, 2, 3, 4, 5)
numbers[-2] # 4

# If you try to pass in an index number that exceeds or equals the length of the tuple, then you will receive an IndexError like this:
# numbers = (1, 2, 3, 4, 5)
# numbers[7]

# Using the tuple() Constructor
developer = 'Jessica'
print(tuple(developer)) # ('J', 'e', 's', 's', 'i', 'c', 'a')

# Checking If an Element Is in a Tuple
programming_languages = ('Python', 'Java', 'C++', 'Rust')

print('Rust' in programming_languages) # True

print('JavaScript' in programming_languages) # False

# Unpacking Values from a Tuple
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

# If you need to collect any remaining elements from a tuple, you can use the asterisk (*) operator like this:
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

# Using Tuples in Simultaneous Assignment
first, second = 10, 20
print(first) # 10
print(second) # 20

# Python evaluates all the expressions on the right side before assigning their values to the variables on the left. This lets you swap two values without a temporary variable:

first, second = 10, 20
first, second = second, first

print(first) # 20
print(second) # 10

# Returning a Tuple from a Function
# A function can return a tuple by placing comma-separated values after return:
def get_coordinates():
    first = 10
    second = 20
    return first, second

coordinates = get_coordinates()
print(coordinates) # (10, 20)

# You can unpack the returned tuple directly into variables:
def get_coordinates():
    first = 10
    second = 20
    return first, second

x, y = get_coordinates()
print(x) # 10
print(y) # 20

# Slicing Tuples
desserts = ('cake', 'pie', 'cookies', 'ice cream')
print(desserts[1:3]) # ('pie', 'cookies')

# Comparing Tuples
# Python compares tuples lexicographically. This means it compares corresponding elements from left to right. The first unequal pair determines the result:
print((1, 9) < (2, 0)) # True

# If the first elements are equal, Python moves to the next pair:
print((1, 3) < (1, 5)) # True

# if all corresponding elements are equal, the shorter tuple is smaller. Tuples with the same length and equal corresponding elements are equal:

print((1, 2) < (1, 2, 3)) # True
print((1, 2) == (1, 2)) # True

# The values in the first unequal pair must support the ordering comparison. Otherwise, Python raises a TypeError:
# print((1, 3) < (1, 'five'))

# Later elements do not need to be comparable if an earlier pair already determines the result:
print((1, 3) < (2, 'five')) # True

# Removing Elements from a Tuple

# If you need to remove an item from a tuple, that isn't possible because tuples are immutable. So this example will produce an error:

# developer = ('Jane Doe', 23, 'Python Developer')
# del developer[1]

# Choosing between Tuples and Lists
# So when might you use a tuple over a list?

# If you need a dynamic collection of elements where you can add, remove, and update elements, then you should use a list. If you know that you are working with a fixed and immutable collection of data, then you should use a tuple.