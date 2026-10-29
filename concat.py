str1 = "Hello"
str2 = " Ayse"

concat = str1 + str2
print(concat)

# repeat using *

str3 = "Ha"
str4 = str3*3
print(str4)

# only works with string
# str5 = "Wife"
# str6 = 4
# print(str5 + 4)

# convert int to str
name = 'John Doe '
age = 26

name_and_age = name + str(age)
print(name_and_age) 

# string interpolation
phrase1 = "Hello"
phrase2 = "Guys"
phrase3 = f'{phrase1}, My name is Faizal, {phrase2}'
print(phrase3)