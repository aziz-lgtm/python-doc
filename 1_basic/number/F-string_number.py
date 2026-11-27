# The expression f"{value:.2f}" displays value with exactly two digits after the decimal point.

value = 12.5

print(f"{value:.2f}") # 12.50
print(value) # 12.5

# another instance
value = 12.3456

print(f"{value:.2f}") # 12.35
print(value) # 12.3456

# Formatting with an F-String Produces a String

value = 12.3456
display = f"{value:.2f}"

print(display) # 12.35
print(value) # 12.3456

print(type(display)) # <class 'str'>
print(type(value)) # <class 'float'>

# How round() Differs from F-String Formatting

value = 12.5

rounded_value = round(value, 2)
formatted_value = f"{value:.2f}"

print(rounded_value) # 12.5
print(formatted_value) # 12.50

# Formatting Doesn't Change the Underlying Value

total = 0.1 + 0.2

print(total) # 0.30000000000000004
print(f"{total:.2f}") # 0.30