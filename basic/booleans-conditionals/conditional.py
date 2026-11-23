# conditional & comparison in python

print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

# if statements
age = 18

if age >= 18:
    print('You are an adult') # You are an adult

# indentation is important in python, these codes would be error:
# age = 18

# if age >= 18:
# print('You are an adult')

# Adding an else Clause
age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet


# Note that you cannot place any statements between the if block and the else clause. The following code would raise a SyntaxError:

# age = 12

# if age >= 18:
#     print('You are an adult')
# print('Almost there!')
# else: # SyntaxError: invalid syntax
#     print('You are not an adult yet')

# Adding elif Clauses
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child

    # you can use as many as elif as you want
    