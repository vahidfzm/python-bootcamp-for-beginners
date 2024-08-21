# Python Bootcamp Beginners - Lesson 1.4 - Conditional Statements, Functions, Iterators 



## Conditional Statements


### Comparison operators
- `==`: equal
- `!=`: not equal
- `<`: less than
- `>`: greater than
- `>=`: less than or equal to
- `>=`: greater than or equal to
```python
print(5 == 5)
print(5 != 5)
print(5 < 5)
print(5 > 5)
print(5 <= 5)
print(5 >= 5)
```

### Boolean operators
- and: returns True if both statements are true
- or: returns True if one of the statements is true
- not: reverse the result, returns False if the result is true
```python
print(5 == 5 and 5 < 6)
print(5 == 5 or 5 < 6)
print(not 5 == 5)
```


### Conditional statements
```python
age = 25
if age >= 18:
    print('You are an adult')
```


```python
age = 12
if age >= 18:
    print('You are an adult')
else:
    print('You are a minor')
```


```python
age = 14
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a minor')
```


## Functions


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

### Function with parameters
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



## Iterators

Iterations are used to execute a block of code multiple times. In Python, we have two types of iterations:
1. for loop
2. while loop


### For Loop
The for loop is used to iterate over a sequence (e.g., list, tuple, string) or other iterable objects.

```python
for item in iterable:
    statement(s)
```

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```


Looping Through a String

You can iterate over the characters of a string using a for loop.
```python
string = 'hello'
for char in string:
    print(char)
```



### While Loop
The while loop is used to execute a block of code as long as a condition is true.
    

```python
while condition:
    statement(s)
```

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```


### Break Statement

The break statement is used to exit a loop prematurely.
```python
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
# Output: 1, 2, 3
```


### Continue Statement

The continue statement is used to skip the rest of the code inside a loop and continue with the next iteration.
```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
# Output: 1, 2, 4, 5
```


While Loop with break and continue
```python
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    if i == 4:
        break
    i += 1
# Output: 1, 2, 4
```


### Nested Loops

You can use one or more loops inside another loop.
```python
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'pink']
for fruit in fruits:
    for color in colors:
        print(fruit, color)
```



