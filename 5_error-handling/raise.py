# What Is the Raise Statement and How Does It Work?
# Python's raise statement can be used in several ways to trigger exceptions. At its most basic, you can raise built-in exceptions or create custom error messages. Here's a simple example:

def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative

# You can see here that raise is the keyword that triggers an exception.


# The raise statement can also be used to re-raise the current exception, which is particularly useful in exception handling:
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')

# Here the keyword raise (without arguments) re-raises the current exception that's being handled.

# You can create and raise custom exceptions by defining your own exception classes:

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')

# Here you can see custom exception classes inherit from Exception or its subclasses.

# The raise statement can also be used with the from keyword to chain exceptions, showing the relationship between different errors:
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

config = parse_config('config.txt')

# Here you can see that raise ... from None suppresses the original exception context:

# The assert statement checks assumptions while debugging and raises AssertionError when a condition is false. Python can remove assertions when run with -O, so they should not be used for input validation that must always run. Use an explicit condition and raise for those checks.
def calculate_square_root(number):
    if number < 0:
        raise ValueError('Cannot calculate square root of negative number')
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except ValueError as e:
    print(f'Invalid input: {e}')