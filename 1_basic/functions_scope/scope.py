# Python has additional scope rules. For now, focus on local and global scope.
# Here is an example of local and global scope:

tax_rate = 0.1

def calculate_tax(price):
    tax = price * tax_rate
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
# print(tax) # NameError: name 'tax' is not defined


# Reassigning a parameter makes that local name refer to a different object.
def double_number(number):
    number = number * 2
    print(number) # 20

original = 10
double_number(original)
print(original) # 10

# What happens when the last line of this code runs?

def greet():
    message = 'Hello!'
    print(message)

greet()
print(message)