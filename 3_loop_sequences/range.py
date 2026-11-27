# range(), instance: range(start, stop, step)

for num in range(3):
    print(num)
# The integer 3 is not included because the stop argument is non-inclusive
# If a start argument is not specified, then the default is 0.

# Here is an example of generating a sequence of integers between 1 and 4:
for num in range(1, 5):
    print(num)

# But if you want to change that default, then you can use the optional step argument.
for num in range(2, 11, 2):
    print('this is the result:', num)
# If you don't provide any arguments to range(), then you'll get a TypeError:
# range() function only accepts integers as arguments, not floats.

# If you want to generate a sequence of integers in decrementing order, then you can use a negative integer for the step argument, like this:
for num in range(40, 0, -10):
    print('counting 10 steps down:',num)

# A range object is immutable, which means it cannot be changed after it is created. A list is mutable, so you can change its values.

# To generate a list of integers, pass a range to the list() constructor. The list() constructor converts an iterable into a list. Here is an example of generating a list of even integers between 2 and 10:

numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]

# Tracking the Index of a for Loop
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for bahasa in languages:
    print(bahasa)

# But what if you wanted to keep track of the index for each element? Well, one option is to create an index variable and increment it by 1 for each iteration of the loop, like this:

languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1

# Using the enumerate() Function
# While that works, an easier way to do that is by using the enumerate() function. The enumerate() function keeps track of the index for an iterable and returns an enumerate object.
languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages)))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# Now, let's refactor the example from earlier to use the enumerate() function:
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

# Using the zip() Function
# So far we've only been iterating over one list. But what if you need to iterate over multiple iterables in parallel? Well, you can use the zip() function for that, which combines lists into pairs of elements and returns an iterator of tuples.

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, dev_id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {dev_id}')

# The enumerate() and zip() functions are very powerful, and when combined with loops, can make your code much more concise.