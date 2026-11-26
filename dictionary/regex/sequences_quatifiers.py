print('Tab:\tdone')
# This means that a backslash in a regular Python string might be interpreted by Python before the re module ever sees it. Depending on the character that follows, that can change your pattern or make Python display a warning.

# To avoid this, you can use a raw string. You create a raw string by adding the letter r (or R) before the opening quote. Raw strings treat backslashes as literal characters rather than escape sequences:
print(r'Tab:\tdone') # Tab:\tdone

# print(r'Tab:\tdone') # Tab:\tdone
import re

room = 'Room 42B'
print(re.search(r'\d', room))
# <re.Match object; span=(5, 6), match='4'>
# \d only matches a single digit: Unlike a quantifier like \d+ (which matches one or more digits in a row), plain \d matches just one digit character (0–9).
import re

room = 'Room 42B'
print(re.search(r'\d+', room))
# <re.Match object; span=(5, 7), match='42'>

# Here are other common quantifiers:

# * matches the preceding character zero or more times.

# ? matches the preceding character zero or one time, making it optional.

# {n} matches the preceding character exactly n times.

# {n,m} matches the preceding character from n to m times.

import re

print(re.search(r'go*al', 'What a goooal!'))
# <re.Match object; span=(7, 13), match='goooal'>

print(re.search(r'colou?r', 'My favorite color is blue'))
# <re.Match object; span=(12, 17), match='color'>

print(re.search(r'\d{4}', 'Room 4266, built in 197'))
# <re.Match object; span=(18, 22), match='1987'>

# You can combine literal characters, special sequences, and quantifiers in the same pattern. For example, the pattern r'\d+ items' matches one or more digits, followed by a space and the word items. You can also combine it with the re.IGNORECASE flag so that the letters can be either lowercase or uppercase:

import re

cart = 'You have 3 ITEMs in your cart.'
print(re.search(r'\d+ IT', cart, re.IGNORECASE))
# <re.Match object; span=(9, 16), match='3 ITEMS'>