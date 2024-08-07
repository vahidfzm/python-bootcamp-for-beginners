# Python Bootcamp Beginners - Lesson 1.2 - Data Types ,Operators, Variables

## Data Types
Python has several built-in data types, including:
- `int`: integer numbers
- `float`: floating-point numbers
- `str`: strings
- `bool`: boolean values (True or False)
- `list`: ordered collection of items
- `tuple`: ordered collection of items (immutable)
- `dict`: collection of key-value pairs
- `set`: unordered collection of unique items
- `NoneType`: special data type representing the absence of a value (None)

## Variables
```python
name = 'John'
age = 25
print(name)
print(age)
print(name, age)
print(name + ' ' + str(age))
```




## Operators
Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators



### Arithmetic operators
| Operator | Name            | Example  |
|----------|-----------------|----------|
| +        | Addition        | x + y    |
| -        | Subtraction     | x - y    |
| *        | Multiplication  | x * y    |
| /        | Division        | x / y    |
| %        | Modulus         | x % y    |
| **       | Exponentiation  | x ** y   |
| //       | Floor division  | x // y   |


### Assignment operators
| Operator | Example | Same As      |
|----------|---------|--------------|
| =        | x = 5   | x = 5        |
| +=       | x += 3  | x = x + 3    |
| -=       | x -= 3  | x = x - 3    |
| *=       | x *= 3  | x = x * 3    |
| /=       | x /= 3  | x = x / 3    |
| %=       | x %= 3  | x = x % 3    |


### Comparison operators
| Operator | Name                          | Example        |
|----------|-------------------------------|----------------|
| ==       | Equal                         | x == y         |
| !=       | Not equal                     | x != y         |
| >        | Greater than                  | x > y          |
| <        | Less than                     | x < y          |
| >=       | Greater than or equal to      | x >= y         |
| <=       | Less than or equal to         | x <= y         |




### Logical operators
| Operator | Description                              | Example                  |
|----------|------------------------------------------|--------------------------|
| and      | Returns True if both statements are true | x < 5 and x < 10         |
| or       | Returns True if one of the statements is true | x < 5 or x < 4      |
| not      | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |




### Identity operators
| Operator | Description                                     | Example    |
|----------|-------------------------------------------------|------------|
| is       | Returns True if both variables are the same object       | x is y     |
| is not   | Returns True if both variables are not the same object   | x is not y |



### Membership operators
| Operator | Description                                                      | Example    |
|----------|------------------------------------------------------------------|------------|
| in       | Returns True if a sequence with the specified value is present in the object     | x in y     |
| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |





## Print Function
Print function is used to display the output on the screen
```python
print('Hello World')
```

## Input function
Input Function is used to take input from the user
```python
name = input('Enter your name: ')
age = input('Enter your age: ')
print(name)
print(age)
```


## Comments
```python
# This is a single line comment
```
Python ignores string literals that are not assigned to a variable, therefore they can be used as multi-line comments.
```python
'''
This is a multi-line comment
This is a multi-line comment
This is a multi-line comment
'''
```

## Casting


## Working with strings
- Single or Double Quote
- Case Sensitive


Try the following:
```python
# concatenation
print("hello" + "world")

# concatenation strings with space
print("hello" + " world")

# concatenation numbers
print(6 + 5)

# concatenation numbers and strings (error)
# print("hello" + 5)

# multiplication
print('hi!' * 3)

print("hello" + "5")

print("6" + "5")

print("6" + " + "+ "5")

# print the first character of the string
print('Hello, world!'[0])

# print the second character of the string
print('Hello, world!'[1])
```




## Strings

- Escape characters in strings:
```python
print('I\'m a student')
print("I'm a student")
print("I'm a \"student\"")
print("I'm a \nstudent")
print("I'm a \tstudent")
print("I'm a \\student")
```


- String methods
```python
print('The quick brown fox jumps over the lazy dog'.count('o'))
print('The quick brown fox jumps over the lazy dog'.find('o'))
print('The quick brown fox jumps over the lazy dog'.replace('o', '0'))
print('The quick brown fox jumps over the lazy dog'.split(' '))
print('The quick brown fox jumps over the lazy dog'.upper())
print('The quick brown fox jumps over the lazy dog'.lower())
print('The quick brown fox jumps over the lazy dog'.title())
print('           The quick brown fox jumps over the lazy dog   '.strip())
print('The quick brown fox jumps over the lazy dog'.startswith('The'))
print('The quick brown fox jumps over the lazy dog'.endswith('dog'))
print('The quick brown fox jumps over the lazy dog'.islower())
print('The quick brown fox jumps over the lazy dog'.isupper())
print('The quick brown fox jumps over the lazy dog'.istitle())
```

- Indexing and slicing strings
```python
print('The quick brown fox jumps over the lazy dog'[0:5])
print('The quick brown fox jumps over the lazy dog'[-5:])
print('The quick brown fox jumps over the lazy dog'[5:10])
print('The quick brown fox jumps over the lazy dog'[::-1])
print('The quick brown fox jumps over the lazy dog'[0::2])
```



