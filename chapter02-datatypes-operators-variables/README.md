# Python For Beginners - Chapter 2 - Basic Syntax, Data Types ,Operators and Variables


## Variables
```python
name = 'John'
age = 25
print(name)
print(age)
print(name, age)
print(name + ' ' + str(age))
```


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

## Working with strings

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



