# Python For Beginners - Chapter 3 - Conditional Statements








## Comparison operators
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

## Boolean operators
- and: returns True if both statements are true
- or: returns True if one of the statements is true
- not: reverse the result, returns False if the result is true
```python
print(5 == 5 and 5 < 6)
print(5 == 5 or 5 < 6)
print(not 5 == 5)
```


## Conditional statements
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
