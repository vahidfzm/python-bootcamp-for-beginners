# Python For Beginners - Chapter 6 - Iteations


Iterations are used to execute a block of code multiple times. In Python, we have two types of iterations:
1. for loop
2. while loop


## For Loop
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


### Looping Through a String

You can iterate over the characters of a string using a for loop.
```python
string = 'hello'
for char in string:
    print(char)
```



## While Loop
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


## Break Statement

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


## Continue Statement

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


## Nested Loops

You can use one or more loops inside another loop.
```python
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'pink']
for fruit in fruits:
    for color in colors:
        print(fruit, color)
```



