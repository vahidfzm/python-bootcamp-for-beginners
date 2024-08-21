# Python Bootcamp Beginners - Lesson 1.3 - Dictionaries

A dictionary is a collection of key-value pairs. Each key is associated with a value. Dictionaries are unordered, changeable, and indexed.
```python
{'name': 'John', 'age': 30, 'city': 'New York'}
```

It is also possible to create a dictionary using the dict() constructor.
```python
dict(name='John', age=30, city='New York')
dict(apple=2, banana=3, cherry=5)
```
You can access the value of a specific key in a dictionary by using the key (If the key does not exist, you will get a `KeyError`).
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(person['name']) # Output: John
```
You can change the value of a specific key in a dictionary by using the key.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
person['age'] = 40
print(person) # Output: {'name': 'John', 'age': 40, 'city': 'New York'}
```
You can add a new key-value pair to a dictionary by using a new key.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
person['country'] = 'USA'
print(person) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
```
You can remove a key-value pair from a dictionary by using the del keyword.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
del person['city']
print(person) # Output: {'name': 'John', 'age': 30}
```



## Methods
There are several methods that you can use to manipulate dictionaries in Python.
- clear()
 The clear() method is used to remove all key-value pairs from a dictionary.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
person.clear()
print(person) # Output: {}
```
- copy()
The copy() method is used to create a shallow copy of a dictionary.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
person_copy = person.copy()
print(person_copy) # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

- get()
The get() method is used to get the value of a specific key in a dictionary.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(person.get('name')) # Output: John
# If the key does not exist, the get() method will return None.
print(person.get('country')) # Output: None
```
get method can also take a default value as a second argument.
```python
print(person.get('country', 'USA')) # Output: USA
```
- keys()
The keys() method is used to return a list of keys in a dictionary.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(person.keys()) # Output: dict_keys(['name', 'age', 'city'])   
```
You can use the keys() method in a for loop to iterate over the keys in a dictionary.

- values()
The values() method is used to return a list of values in a dictionary.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(person.values()) # Output: dict_values(['John', 30, 'New York'])
```
You can use the values() method in a for loop to iterate over the values in a dictionary.
- pop()
The pop() method is used to remove a key-value pair from a dictionary and return the value.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
name = person.pop('name')
print(name) # Output: John
print(person) # Output: {'age': 30, 'city': 'New York'}
```
If the key does not exist, the pop() method will raise a KeyError.

- popitem()
The popitem() method is used to remove the last key-value pair from a dictionary and return it as a tuple.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
item = person.popitem()
print(item) # Output: ('city', 'New York')
print(person) # Output: {'name': 'John', 'age': 30}
```
If the dictionary is empty, the popitem() method will raise a KeyError.

## Iterating Over a Dictionary
You can use a for loop to iterate over the key-value pairs in a dictionary.
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(key, value)
# Output:
# name John
# age 30
# city New York
```
You can also use a for loop to iterate over the keys in a dictionary.
```python
for key in person.keys():
    print(key, person[key])
# Output:
# name John
# age 30
# city New York
```
## Merge Dictionaries:
```python
dict1 ={'a': 1, 'b': 2}
dict2= {'b': 3, 'c': 4}

merged = {**dict1, **dict2}
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}

```



## Dictionary Comprehension
Dictionary comprehension is a concise way to create dictionaries in Python.
```python
squares = {x: x*x for x in range(6)}    
print(squares) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
You can also use dictionary comprehension to filter items in a dictionary.
```python
squares = {x: x*x for x in range(6) if x % 2 == 0}
print(squares) # Output: {0: 0, 2: 4, 4: 16}
```
You can use dictionary comprehension to create dictionaries from two lists.
```python
keys = ['name', 'age', 'city']
values = ['John', 30, 'New York']
person = {keys[i]: values[i] for i in range(len(keys))}
print(person) # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```
another example:

```python
original_dict = {'a': 1, 'b': 2, 'c': 3}
uppercased_keys = {k.upper(): v for k, v in original_dict.items()}
print(uppercased_keys) # Output: {'A': 1, 'B': 2, 'C': 3}
```