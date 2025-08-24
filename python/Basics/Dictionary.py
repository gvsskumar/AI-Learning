#Dictionary

#Dictionary Types
dict1 = {'name': 'Surya', 'age': 20, 'city': 'Hyderabad'}
print(dict1)

#Accessing Dictionary Elements
dict1 = {'name': 'Surya', 'age': 20, 'city': 'Hyderabad'}
print(dict1['name'])  # Output: Surya
print(dict1['age'])  # Output: 20
print(dict1['city'])  # Output: Hyderabad

#Adding Elements to a Dictionary
dict1 = {'name': 'Surya', 'age': 20, 'city': 'Hyderabad'}
dict1['country'] = 'India'
print(dict1)

#Removing Elements from a Dictionary
dict1 = {'name': 'Surya', 'age': 20, 'city': 'Hyderabad'}
del dict1['name']
print(dict1)

#Dictionary Methods
# clear(): Removes all elements from the dictionary
# copy(): Returns a copy of the dictionary
# get(): Returns the value of the specified key if it exists, otherwise returns None
# items(): Returns a list of tuples containing the key-value pairs of the dictionary
# keys(): Returns a list of the keys of the dictionary
# values(): Returns a list of the values of the dictionary

#Dictionary unpacking
dict1 = {'name': 'Surya', 'age': 20, 'city': 'Hyderabad'}
name, age, city = dict1
print(name)  # Output: Surya
print(age)  # Output: 20
print(city)  # Output: Hyderabad

#Dictionary Methods Examples
dict1 = {'name': 'Surya', 'age': 20, 'city': 'Hyderabad'}
dict1.clear()  # Output: {}
dict1.copy()  # Output: {'name': 'Surya', 'age': 20, 'city': 'Hyderabad'}
dict1.get('name')  # Output: Surya
dict1.items()  # Output: dict_items([('name', 'Surya'), ('age', 20), ('city', 'Hyderabad')])
dict1.keys()  # Output: dict_keys(['name', 'age', 'city'])
dict1.values()  # Output: dict_values(['Surya', 20, 'Hyderabad'])

#Dictionary update
dict1 = {'name': 'Surya', 'age': 20, 'city': 'Hyderabad'}
dict2 = {'country': 'India', 'state': 'Telangana'}
dict1.update(dict2)
print(dict1)
