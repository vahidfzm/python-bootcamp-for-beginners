
#  Chapter 6 Exercises

``
1. Define a function called `filter_even_numbers` that takes a list of integers as input and returns a new list containing only the even numbers from the original list.
```python
# filter_even_numbers([1, 2, 3, 4, 5, 6,23,46,77]) => [2, 4, 6,46]
```
2. Create a function named `remove_duplicates` that takes a list as input and returns a new list with all duplicate elements removed.
```python
# remove_duplicates([1, 2, 3, 4, 2, 3, 5]) => [1, 2, 3, 4, 5]
```
3. Define a function named `list_intersection` that takes two lists as input and returns a new list containing only the elements that are common to both lists.
```python
# list_intersection([1, 2, 3, 4], [3, 4, 5, 6]) => [3, 4]
```
4. Extend the function in the exercise no.1 as:
   - Return an empty list if the input is not a list.
   - Ignore non-integer elements in the input list.
```python
# filter_even_numbers([1, 2, 3, 4, 5, 6]) => [2, 4, 6]
# filter_even_numbers([1, 'a', 2, 'b', 3, 4]) => [2, 4]
# filter_even_numbers('hello') => []
# filter_even_numbers(12345) => []  
```
