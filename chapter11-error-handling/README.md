# Python For Beginners - Chapter 11 - Error Handling

To control the flow of the program when an error occurs, we can use error handling techniques.

Python provides several built-in exceptions that can be raised when an error occurs.

We can use the `try`, `except`, `else`, and `finally` keywords to handle exceptions in Python.

```python
try:
    # code that may raise an exception
except:
    # code to handle the exception
else:
    # code to run if no exception is raised
finally:
    # code to run regardless of whether an exception is raised or not
```

Example:

```python
try:
    # code that may raise an exception
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print("You entered:", x)
finally:
    print("Program completed.")
```

It is possible to define multiple except blocks to handle different exceptions.

```python
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", y)
finally:
    print("Program completed.")
```

If the exception type is not specified, the except block will catch all exceptions.
    
```python
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except:
    print("An error occurred.")
```

We can raise exceptions using the `raise` keyword in Python. This allows us to create custom exceptions and control the flow of the program.

```python
try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("Number cannot be negative.")
except ValueError as e:
    print(e)
else:
    print("You entered:", x)
```

## Assert Statements
We can use the `assert` statement to check conditions in the code. 

If the condition is false, an `AssertionError` is raised.

```python
x = -10
assert x > 0, "x must be greater than 0"
print("x is:", x)
# output: AssertionError: x must be greater than 0
```
The message after the comma is optional and can be used to provide additional information about the assertion.


-----

list of built-in exceptions: https://docs.python.org/3/library/exceptions.html


