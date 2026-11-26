# Creating a Set
my_set = {1, 2, 3, 4, 5}
print(my_set)
# One quirk of working with sets is that, if you ever need to define an empty set, you must use the set() function. If you just write empty curly braces, like {}, Python will automatically create a dictionary.


# Adding Elements to a Set
my_set.add(6)
print(my_set)

# Removing Elements From a Set
# To remove an element from the set, you have two options. You can either use the .remove() method or the .discard() method, and pass in the element that you want to remove as argument.

# The .remove() method will raise a KeyError if the element is not found, while the .discard() method will not:
print(my_set.remove(4))
print(my_set.discard(4))

# The .clear() method removes all the elements from the set:
print(my_set.clear())

# Comparing Sets
# The .issubset() and the .issuperset() methods check if a set is a subset or superset of another set, respectively.

# Here, we are checking if your_set is a subset of my_set, which is False because not all the elements of your_set are in my_set.

# We are also checking if my_set is a superset of your_set. This is also False because my_set does not have all the elements of your_set:

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

# The .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common. In this case, that's False because my_set and your_set do have common elements – 2, 3, and 4:
print(my_set.isdisjoint(your_set)) # False

# Using Set Operators
# The union operator | returns a new set with all the elements from both sets:
my_set | your_set # {1, 2, 3, 4, 5, 6}

# The intersection operator & returns a new set with only the elements that the sets have in common:
my_set & your_set # {2, 3, 4}

# The difference operator - returns a new set with the elements of the first set that are not in the other sets. In this example, the numbers 1 and 5 are in my_set but NOT in your_set:
my_set - your_set # {1, 5}

# The symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both. In this case, 1 and 5 are in my_set but not in your_set, so they are included. And the number 6 is in your_set but not in my_set, so it's included as well:
my_set ^ your_set # {1, 5, 6}

# Each one of these operators also has its corresponding compound assignment operator if you add the equal sign next to it. These operators automatically assign the resulting set to the first set in the expression:
# |= &= -= ^=
# For example, the -= operator finds the difference between the sets and updates the first set with that result:
my_set ^= your_set
print(my_set) # {1, 5}

# Checking If an Element Is in a Set
print(5 in my_set)