pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# Another alternative would be using the dict() constructor, which builds the dictionary from a sequence of key-value pairs.

pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

# Accessing Dictionary Values
print(pizza['name'])#Margherita Pizza

# Updating Dictionary Values
pizza['name'] = 'Margherita'
print(pizza['name'])

# Dictionary Methods; dictionary.get(key, default)
print('result', pizza.get('toppings', [])) # ['mozzarella', 'basil']
# In this example, if the toppings key doesn't exist, it will return an empty list, which is the default value that we are passing here as the second argument. But if toppings does exist, it will return that value:

# The .keys() and .values() methods return a view object with all the keys and values in the dictionary, respectively:

print(pizza.keys())
# dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])

print(pizza.values())
# dict_values(['Margherita', 8.9, 250, ['mozzarella', 'basil']])

# .items() method returns a view object with all the key-value pairs in the dictionary, including both the keys and the values:

print('hasil:',pizza.items())
# dict_items([('name', 'Margherita'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

# .clear() method removes all the key-value pairs from the dictionary:

pizza.clear()

# The .pop() method removes the key-value pair with the key that you specify as the first argument and returns its value. If the key doesn't exist, it returns the default value that you specify as the second argument. If the key doesn't exist and you don't pass a default value, a KeyError is raised
print('hasil', pizza.pop('price', 10))
# pizza.pop('total_price') # KeyError

# In Python 3.7 and more recent versions, the .popitem() method removes the last inserted item:
# print(pizza.popitem())

# .update() method updates the key-value pairs with the key-value pairs of another dictionary. If they have keys in common, their values are overwritten. But total_time is new, so it will be added to the pizza dictionary as a new key-value pair:
print('result: ha haha',pizza.update({ 'price': 15, 'total_time': 25 }))
print(pizza)

