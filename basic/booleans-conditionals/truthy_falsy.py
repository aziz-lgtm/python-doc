# While those are very powerful, you will often run into situations where you need to compare multiple values at once. This can lead to nested conditional statements, for example:
is_citizen = False
age = 5

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
    else:
        print('You arent eligible to vote')
else:
    print('You are not eligible to vote')

# check whether truthy or falsy
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True


# The and Operator
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

# The or operator
age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

    # the not operator; It converts truthy values to False and falsy values to True.

    print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

# It is common to use the not operator in conditionals to check whether a value is falsy, like this:
is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')