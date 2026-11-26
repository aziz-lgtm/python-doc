import re

sentence = 'The cat sat on the mat.'
print(re.search('cat', sentence))
# <re.Match object; span=(4, 7), match='cat'>

# import re

sentence = 'The cat sat on the mat.'
print(re.search('cat', sentence))
# <re.Match object; span=(4, 7), match='cat'>
import re

sentence = 'The cat sat on the mat.'
result = re.search('cat', sentence)

print(result.group()) # cat
print(result.span())  # (4, 7)

# When the pattern is not found, re.search returns None:
import re

sentence = 'The cat sat on the mat.'
print(re.search('dog', sentence)) # None

# By default, regex matching is case sensitive. This means that the pattern 'Cat' does not match the text cat:
import re

sentence = 'The cat sat on the mat.'
print(re.search('Cat', sentence)) # None

# To change how a pattern is matched, you can pass a flag as the third argument to re.search. The re.IGNORECASE flag makes the search case insensitive, so uppercase and lowercase letters are treated as the same:
import re

sentence = 'The cat sat on the mat.'
print(re.search('Cat', sentence, re.IGNORECASE))
# <re.Match object; span=(4, 7), match='cat'>