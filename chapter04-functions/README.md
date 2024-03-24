# Python For Beginners - Chapter 3 - Functions



To define a function we use the `def` keyword
```python
def function_name():
    code
```

Example:
```python
def hello():
    print('Hello')

hello()
```

## Function with parameters
```python
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



## Built-in functions
Python has a number of built-in functions that are available for use without the need to import any module. Some of the most commonly used built-in functions are:


1. print() - used to print the output to the console
2. input() - used to take input from the user
3. len() - used to get the length of a string, list, tuple, dictionary, etc.
4. range() - used to generate a sequence of numbers
5. type() - used to get the type of an object
6. int() - used to convert a string or a number to an integer
7. float() - used to convert a string or a number to a float