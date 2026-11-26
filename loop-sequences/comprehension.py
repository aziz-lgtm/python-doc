# What Are List Comprehensions and What Are Some Useful Functions to Work with Lists?
# lesson before
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# list comprehension; Here is the refactored example from earlier using square brackets:
even_numbers = [num for num in range(21) if num % 2 == 0]
print('result:',even_numbers)

# Using Conditional Expressions in List Comprehensions
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print('result2 :',result)

# Filtering Lists with filter()

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print('destination:',long_words) # ['mountain', 'river', 'cloud']

# Transforming Lists with map()
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32 #In Python 3, the single slash / is true division and always returns a float, even when the division comes out evenly

fahrenheit = list(map(to_fahrenheit, celsius))
print('result3 :',fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# Adding Up Values with sum()
# The last function we will look at is the sum() function. This function is used to get the sum from an iterable like a list or tuple. Here is an example of using the sum() function:
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50

# You can also pass in an optional start argument which sets the initial value for the summation. Here is an updated example using the start argument as a positional argument:
numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total) # 60

# You can also choose to use the start argument as a keyword argument like this instead:
numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total) # 60
