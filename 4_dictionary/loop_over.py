products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

# Looping Over Values
for price in products.values():
    print(price)

# Looping Over Keys
for product in products.keys():
    print(product)

# Or

for product in products:
    print(product)

# Looping Over Key-Value Pairs
for product in products.items():
    print(product)

# Here, we are defining a product loop variable and a price loop variable. Each one will hold its corresponding value. It's important to define them in order – the key first, and then the value:

for product, price in products.items():
    print(product, price)

# Applying Changes to Every Value in a Key-Value Pair
for product, price in products.items():
    products[product] = round(price * 0.8)

print('price after discount 20% :',products)

# {
#     'Laptop': 792, 
#     'Smartphone': 480, 
#     'Tablet': 200, 
#     'Headphones': 56
# }

# Using enumerate() to Track a Counter
for product in enumerate(products):
    print(product)

# If you need to, you can assign these values to separate loop variables. Here, we have two loop variables (index and product). This is what you will commonly see and use when you work with enumerate():
for i, product in enumerate(products):
    print(i, product)

# Using enumerate() with Values and Items
# If you need to iterate over the values, you can replace products by products.values():
for price in enumerate(products.values()):
    print(price)

# You can assign them to separate loop variables as well:
for index, price in enumerate(products.values()):
    print(index, price)

# And with products.items(), you can get the entire key-value pair in addition to the "index" or "counter":
for index, product in enumerate(products.items()):
    print(index, product)

# Customizing the Starting Count
for index, product in enumerate(products.items(), 1):
    print(index, product)
# You can see this change in the output. Now the first integer is 1 instead of 0:
# 1 ('Laptop', 990)
# 2 ('Smartphone', 600)
# 3 ('Tablet', 250)
# 4 ('Headphones', 70)