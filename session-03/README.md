# Python Bootcamp - Session 03 - Strings, Variables, Functions



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



## Variables
```python
name = 'John'
age = 25
print(name)
print(age)
print(name, age)
print(name + ' ' + str(age))
```



## Input function
```python
name = input('Enter your name: ')
age = input('Enter your age: ')
print(name)
print(age)
```

## Functions
```python
def hello():
    print('Hello')

hello()

def greet(name):
    print('Hello', name)

greet('John')

def greet(name, age):
    print('Hello', name, 'you are', age, 'years old')

greet('John', 25)
```



### Return statement
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

### Default arguments in functions
```python
def greet(name, age=25):
    print('Hello', name, 'you are', age, 'years old')

greet('John')
greet('John', 30)
```



### Keyword arguments 
Keyword arguments or named arguments are used to pass the values to the function parameters by specifying the parameter name
```python
def greet(name, age):
    print('Hello', name, 'you are', age, 'years old')

greet(age=25, name='John')
```