my_str = 'heLLo world'

uppercase = my_str.upper()
print(uppercase)
lower = my_str.lower()
print(lower)

# strip()
str1 = '  hello world  '
trimmed = str1.strip()
print(trimmed)

# replace(old, new)
str2 = 'hwllo world'
strNew = str2.replace('hwllo', 'hello')
print(strNew)

# split()
str3 = 'hello world'
splitW = str3.split()
print(splitW)

# join()
str4 = ['hello', 'world']
joined = ' '.join(str4)
print(joined)

# startswith() & endswith()
str5 = 'hello world'
startsW = str5.startswith('hello')
print(startsW)

endsW = str5.endswith('world')
print(endsW)

# find()

str6 = 'hello world'
index = str6.find('bad')
print(index)

# count()
str7 = 'hello world'
count = str7.count('l')
print(count)

# capitalize()
str8 = 'hello world'
cap = str8.capitalize()
print(cap)

# isupper()
my_str = 'OLX'

is_all_lower = my_str.isupper()
print(is_all_lower)  # True

my_st = 'hello world'

is_all_lowe = my_st.islower()
print(is_all_lowe)

# title()
str10 = 'hello world'
title = str10.title()
print(title)
