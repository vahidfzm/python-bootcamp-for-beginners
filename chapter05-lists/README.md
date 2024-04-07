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

## Range Function
```python
range(start, stop, step)
```
The range() function generates a sequence of numbers from the start value to the stop value with the specified step value.
```python
print(list(numbers)) # Output: [0, 1, 2, 3, 4]
numbers = range(1, 6)
print(list(numbers)) # Output: [1, 2, 3, 4, 5]
numbers = range(1, 6, 2)
print(list(numbers)) # Output: [1, 3, 5]
```

The return value of the range() function is a range object, which is an iterable sequence of numbers and can be iterated using a for loop.
```python
numbers = range(5)
for number in numbers:
    print(number)
# Output:
# 0
# 1
# 2
# 3
# 4
```
If you want to convert the range object to a list, you can use the list() function.
```python
numbers = range(5)
print(list(numbers)) # Output: [0, 1, 2, 3, 4]
```



## List Comprehension

List comprehension is a concise way to create lists in Python. It allows you to create a new list by applying an expression to each element in an existing list.
```python
[expression for item in iterable]
```
Example:
```python
numbers = [1, 2, 3, 4, 5]
squares = [x*x for x in numbers]
print(squares) # Output: [1, 4, 9, 16, 25]
```
You can also use list comprehension to filter items in a list.
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers) # Output: [2, 4]
```
You can use list comprehension to create lists from strings.

```python
sentence = 'Hello, World!'
letters = [char for char in sentence if char.isalpha()]
print(letters) # Output: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
```
or:
```python
sentence = 'Hello, World'
vowels = [char for char in sentence if char in 'aeiouAEIOU']
print(vowels) # Output: ['e', 'o', 'o']
```