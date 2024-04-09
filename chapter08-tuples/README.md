# Python For Beginners - Chapter 8 - Tuples


Tuples are immutable sequences, used to store collections of data.

Tuples are constructed by the comma operator (not within square brackets), with or without enclosing parentheses, but an empty tuple must have the enclosing parentheses, such as a, b, c or ().

A single item tuple must have a trailing comma, such as (d,).
```python
t = 12345, 54321, 'hello!'
print(t[0]) # Output: 12345
print(t) # Output: (12345, 54321, 'hello!')
```
Tuples may be nested:

```python
u = t, (1, 2, 3, 4, 5)
print(u) # Output: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
```

tuple function can be used to convert other sequences to tuples:
```python
print(tuple([1, 2, 3])) # Output: (1, 2, 3)
print(tuple('hello')) # Output: ('h', 'e', 'l', 'l', 'o')
```

## Tuples vs Lists
Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

Tupels are faster than lists.

# Usful links:
1- https://www.youtube.com/watch?v=NI26dqhs2Rk
