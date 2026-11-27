# The count() Method
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count('Rust')) # 2
print(programming_languages.count('Golang')) # 2
# If no arguments are passed into the count() method, then Python raises a TypeError:

# The index() Method
print(programming_languages.index('Java')) # 2
# If the specified item cannot be found, then Python raises a ValueError:

# Another thing you can do with the index() method is to pass in optional start and stop index arguments. Here is an example of passing in an optional start index:

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3)) # 5

# You can also pass in an optional stop index. Here is a modified example of specifying a start and stop index:
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages.index('Python', 2, 5)) # 2

# The sorted() Function
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(sorted(numbers)) # [2, 3, 7, 13, 18, 45, 67, 78]

# If you need to customize the sorting behavior for an iterable, you can use the optional reverse and key arguments. Here is an example of using the key argument to sort items in a tuple by length:
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, key=len))

# reverse()
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Conclusion
# Tuples are a common data type in Python. Understanding how to work with them, along with some helpful methods and functions, will help you write more efficient code