  # Checking for None
# You can use is None to check whether a value is missing, or is not None to check whether it is present:

response = None

print(response is None) # True
print(response is not None) # False

# None is falsy, but it is not the same object as False. For example, a response could be True for yes, False for no, or None if no answer has been given:

# more detail instance
response = False

if response is None:
    print('No answer yet')
else:
    print('An answer was given') # An answer was given

    # Using if not response instead would treat both False and None alike. The identity check distinguishes a negative answer from a missing answer:

    response = False

if not response is None:
    print('No answer yet')
else:
    print('An answer was given')

    # You can also use identity to check specifically for the boolean objects:
    response = False

print(response is True) # False
print(response is False) # True
print(response is not None) # True
# These checks ask whether response is exactly True, False, or an object other than None. They do not simply test truthiness.