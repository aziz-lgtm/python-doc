# The match Function
import re

print(re.match(r'\d+', '42 apples'))
# <re.Match object; span=(0, 2), match='42'>

print(re.match(r'\d+', 'apples: 42')) # None

# The fullmatch, r'\d+:\d+'
# Function
import re

user_input = '10:30pm'
print(re.search(r'\d+:\d+', user_input))
# <re.Match object; span=(0, 5), match='10:30'>

# When you are validating data, you usually want the whole string to follow the pattern. For that, you can use the fullmatch function. It returns a match object only when the pattern matches the entire string, and None otherwise:
import re

print(re.fullmatch(r'\d+:\d+', '10:30pm')) # None

print(re.fullmatch(r'\d+:\d+', '10:30'))
# <re.Match object; span=(0, 5), match='10:30'>

# The findall Function
import re

menu = 'Coffee costs 3 dollars, tea costs 2, and cake costs 5.'
print(re.findall(r'\d+', menu)) # ['3', '2', '5']

# The sub Function
import re

message = 'My phone number is 555 0123'
print(re.sub(r'\d', '*', message))
# My phone number is *** ****


# sub also has two optional parameters. The first one is count, which limits how many matches get replaced:

import re

message = 'My phone number is 555 0123'
print(re.sub(r'\d', '*', message, count=3))
# My phone number is *** 0123

# The second one is flags. Like the other functions, sub can use flags such as re.IGNORECASE:
import re

sentence = 'Cat and cat'
print(re.sub('cat', 'dog', sentence, flags=re.IGNORECASE))
# dog and dog