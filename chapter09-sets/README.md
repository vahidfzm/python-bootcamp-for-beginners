# Python For Beginners - Chapter 9 - Sets

A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.


Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.
```python
basket = {'apple', 'orange', 'pear', 'banana'}
print(basket) # Output: {'orange', 'banana', 'pear', 'apple'}
```
Sets can be created from lists, strings, and other sequences:
```python
a = set('abracadabra')
print(a) # Output: {'a', 'r', 'b', 'c', 'd'}

b = set(['a', 'b', 'c', 'd', 'a'])
print(b) # Output: {'a', 'b', 'c', 'd'}
```

Duplicates are removed in the set.
```python
c = set(['a', 'b', 'c', 'd', 'a'])
print(c) # Output: {'a', 'b', 'c', 'd'}
```

Check if item is in a set
```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('orange' in basket) # Output: True
```

## Adding and removing elements
```python
a = {1, 2, 3}
a.add(4)
print(a) # Output: {1, 2, 3, 4}

a.remove(3)
print(a) # Output: {1, 2, 4}
```

## Set operations
```python
a = set('abracadabra')
b = set('alacazam')
print(a) # Output: {'a', 'r', 'b', 'c', 'd'}
print(b) # Output: {'a', 'l', 'c', 'z', 'm'}
```

letters in a but not in b
```python
print(a - b) # Output: {'r', 'd', 'b'}
```
letters in a or b or both
```python
print(a | b) # Output: {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
```
letters in both a and b
```python
print(a & b) # Output: {'a', 'c'}
```
letters in a or b but not both
```python
print(a ^ b) # Output: {'r', 'd', 'b', 'm', 'z', 'l'}
```

## Set comprehensions
```python
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # Output: {'r', 'd'}
```

## loop over a set
```python
a = {1, 2, 3}
for x in a:
    print(x) # Output: 1 2 3
```

