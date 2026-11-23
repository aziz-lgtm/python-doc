# integer

int_one = 1
int_two = -2

print(type(int_one))
print(type(int_two))

sum_integer = int_one + int_two
print('Result of the sum:', sum_integer)
sum_integer2 = int_one * int_two
print('Result of the multiplication:', sum_integer2)
sum_integer3 = int_one / int_two
print('Result of the division', sum_integer3)

# floor division operation
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats)

# exponentiation

gain_one = 300
time_frame = 3
total = gain_one ** time_frame
print('Profit realised:', total)

# Converting Data into Integers or Floats
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)  # 56.0
print(type(my_float_1))  # <class 'float'>

# The int() function returns an integer constructed from the given number:
my_float = 12.92563
my_int = int(my_float)

print(my_int)  # 12

# Also, you can use the same built-in functions to convert a string into either a float or integer:
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>

# The float() function can also create a special value that represents positive infinity when you pass it the string 'inf'. Positive infinity is greater than any finite integer or float:
infinity = float('inf')

print(infinity)  # inf
print(type(infinity))  # <class 'float'>

# round():
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

# abs(): Returns the absolute value of a number:
num = -15

absolute_value = abs(num)
print(absolute_value) # 15

# pow(): raises a number to the power of another or performs modular exponentiation.

result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3
