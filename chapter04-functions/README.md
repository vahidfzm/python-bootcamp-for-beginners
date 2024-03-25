# Python For Beginners - Chapter 4 - Functions



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

Write a function (named 'is_adult') that takes an integer (named 'age') as an argument and returns True if the number is greater than or equal to 18 and False otherwise
```python
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

print is_adult(15)
print is_adult(35)
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

### Variable number of arguments
```python
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
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