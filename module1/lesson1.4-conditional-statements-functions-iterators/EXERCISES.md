
#  Lesson 1.4 Exercises

1. Write a function named `add` that takes two arguments and returns their sum
2. Write a function named `greet` that takes a name and an age as arguments and prints a greeting message (e.g. `Hello John, you're 25 years old`)
3. Write a function (named `longest_string`) that takes 2 strings as arguments and returns the longest string.
4. Develop a function called `vowel_check` that takes a character (a single letter) as input and returns True if it's a vowel (a, e, i, o, u), and False otherwise.
5. Create a function named `calculate_pay` which accepts the number of extra hours worked and calculates the total pay. The regular hourly rate for the first 40 hours is $20, and for any additional hours, the rate increases to $30. 
6. Create a function named `reverse_string` that takes a string as input and returns the reverse of that string.
7. Create a function called `format_name` that takes three arguments: first name, last name, and an optional prefix (default value None). It returns the full name formatted as "Prefix FirstName LastName" if prefix is provided, or "FirstName LastName" if no prefix is provided.
8. Define a function called `filter_even_numbers` that takes a list of integers as input and returns a new list containing only the even numbers from the original list.
```python
# filter_even_numbers([1, 2, 3, 4, 5, 6,23,46,77]) => [2, 4, 6,46]
```
9. Create a function named `remove_duplicates` that takes a list as input and returns a new list with all duplicate elements removed.
```python
# remove_duplicates([1, 2, 3, 4, 2, 3, 5]) => [1, 2, 3, 4, 5]
```
10. Define a function named `list_intersection` that takes two lists as input and returns a new list containing only the elements that are common to both lists.
```python
# list_intersection([1, 2, 3, 4], [3, 4, 5, 6]) => [3, 4]
```
11. Extend the function in the exercise no.1 as:
   - Return an empty list if the input is not a list.
   - Ignore non-integer elements in the input list.
```python
# filter_even_numbers([1, 2, 3, 4, 5, 6]) => [2, 4, 6]
# filter_even_numbers([1, 'a', 2, 'b', 3, 4]) => [2, 4]
# filter_even_numbers('hello') => []
# filter_even_numbers(12345) => []  
```

