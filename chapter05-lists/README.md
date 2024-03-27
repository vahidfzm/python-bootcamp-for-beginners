# Python For Beginners - Chapter 5 - Lists


A list is a sequence of elements. Each element can be of any type. The elements in a list are indexed starting from 0.

```python
[1,2,3,4,5]
['apple', 'banana', 'cherry']
[1, 2, 3, 4, 5, 'Hello', 3.14, True]
```
nested list:
```python
['apple', [1, 2, 3], 'banana']
```

## List Indexing
List indexing is used to access an element in a list. The index of the first element is 0, the index of the second element is 1, and so on.
```python
fruits = ['apple', 'banana', 'cherry']
fruits[0] # Output: 'apple'
fruits[1] # Output: 'banana'
fruits[2] # Output: 'cherry'
fruits[-1] # Output: 'cherry'
```

## Changing List Elements
You can change the value of a specific element in a list by using the index.
```python
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'orange'
print(fruits) # Output: ['apple', 'orange', 'cherry']
```


## List Operations
- Concatenation
```python
fruits = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'potato', 'spinach']
print(fruits + vegetables) # Output: ['apple', 'banana', 'cherry', 'carrot', 'potato', 'spinach']
```
- Repetition
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits * 2) # Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']
```


## List Slicing
```python
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
print(fruits[1:4]) # Output: ['banana', 'cherry', 'date']
print(fruits[:4]) # Output: ['apple', 'banana', 'cherry', 'date']
print(fruits[4:]) # Output: ['elderberry', 'fig']
print(fruits[:]) # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
print(fruits[-3:-1]) # Output: ['date', 'elderberry']
print(fruits[-3:]) # Output: ['date', 'elderberry', 'fig']
print(fruits[:-3]) # Output: ['apple', 'banana', 'cherry']
print(fruits[::-1]) # Output: ['fig', 'elderberry', 'date', 'cherry', 'banana', 'apple']
```



## String to List

You can convert a string to a list by using the list() function.
```python
string = 'hello'
lst = list(string)
print(lst) # Output: ['h', 'e', 'l', 'l', 'o']
```


## Splitting a String

You can split a string into a list of substrings by using the split() method.
```python
string = 'apple,banana,cherry'
lst = string.split(',')
print(lst) # Output: ['apple', 'banana', 'cherry']
```

## List methods
- append()

The append() method is used to add an element to the end of a list.
```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')
print(fruits) # Output: ['apple', 'banana', 'cherry', 'date']
```


- insert()

The insert() method is used to add an element at a specific index in a list.
```python
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'date')
print(fruits) # Output: ['apple', 'date', 'banana', 'cherry']
```


- remove()

The remove() method is used to remove a specific element from a list.
```python
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits) # Output: ['apple', 'cherry']
```
- pop()

The pop() method is used to remove an element at a specific index from a list.    
```python
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
```
the pop() method returns the removed element.

If you don't specify an index, the pop() method will remove the last element.


- clear()

The clear() method is used to remove all elements from a list.
```python
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits) # Output: []
```
- index()

The index() method is used to get the index of a specific element in a list.
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana')) # Output: 1
```

- count()

The count() method is used to count the number of occurrences of a specific element in a list.
```python
fruits = ['apple', 'banana', 'cherry', 'banana']
print(fruits.count('banana')) # Output: 2
```

- sort()

The sort() method is used to sort the elements of a list in ascending order.
```python
fruits = ['cherry', 'apple', 'banana']
fruits.sort()
print(fruits) # Output: ['apple', 'banana', 'cherry']
```

- reverse()

The reverse() method is used to reverse the order of the elements in a list.
```python
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits) # Output: ['cherry', 'banana', 'apple']
```

- copy()

The copy() method is used to create a copy of a list.
```python
fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
print(fruits_copy) # Output: ['apple', 'banana', 'cherry']
```

- extend()

The extend() method is used to add the elements of one list to another list.
```python
fruits = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'potato', 'spinach']
fruits.extend(vegetables)
print(fruits) # Output: ['apple', 'banana', 'cherry', 'carrot', 'potato', 'spinach']
```

- list()

The `list` function is used to create a list from an iterable object.
```python
fruits = list(('apple', 'banana', 'cherry'))
print(fruits) # Output: ['apple', 'banana', 'cherry']
```

- len()

The len() function is used to get the number of elements in a list.
```python
fruits = ['apple', 'banana', 'cherry']
print(len(fruits)) # Output: 3
```

