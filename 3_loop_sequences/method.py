# append()
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

# you can even add one list inside
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

# Adding Multiple Elements with extend()

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]
# Inserting Elements at a Specific Index, insert()
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]

# remove()
numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50]

# To remove an element at a specific index in the list, you can use the pop()
numbers = [1, 2, 3, 4, 5]
print(numbers.pop(1)) # The number 2 is returned

# If you don't specify an index for the pop method, then the last element is removed.
numbers = [1, 2, 3, 4, 5]
print(numbers.pop())

# Clearing a List, clear()

numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers) # []

# Sorting a List
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]

# shorted()
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

# Reversing a List, reverse()
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]

# Finding the Index of an Element, index()
programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(programming_languages.index('Java')) # 1

# If the element cannot be found, then Python throws a ValueError
