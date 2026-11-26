def square(num):
    return num ** 2

print(square(4)) # 16

# Here's what the square() function looks like when refactored into a lambda function:
lambda num: num ** 2
# Lambda functions are great when you need to use them in higher-order functions like this:
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# it is not a good practice to assign a lambda function to a variable like this:
numbers = [1, 2, 3, 4, 5]

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]

# This defeats the purpose of using anonymous functions. In this case, you should use a regular function, like this:
numbers = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]

# Also, you should avoid creating lambda functions that are difficult to read or unnecessarily complicated, like this
result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
print(result)  # 14

# In this case, it would be better to create a separate function with an if/else statement, and then call that function:
def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print('result: ',calculate_expression(3))  # 14

# Both regular functions and lambda functions have their use cases in Python programs. If you are dealing with a single inline expression, then you might consider using a lambda function. Otherwise, using a regular function would be the way to go.
