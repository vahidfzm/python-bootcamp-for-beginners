
#  Lesson 1.3 Exercises



1. Remove duplicates from the following list, by converting it to a `Set`
```python
list1 = [1,1,5,5,4,3,7,7,8,9]
```
2. Remove duplicates from the following list, without using `Sets`
```python
list1 = [1,1,5,5,4,3,7,7,8,9]
```

3. Use a list comprehension to select all movies that start with the letter 'M'
```python
movies = [
    "The Matrix", "Mad Max: Fury Road", "Memento", "The Godfather", 
    "Moonlight", "Inception", "Manchester by the Sea", "Gladiator", 
    "Mulan", "Pulp Fiction", "Minari", "The Dark Knight", 
    "Moulin Rouge!", "Interstellar", "Monsters, Inc.", "Titanic", 
    "Murder on the Orient Express", "The Shawshank Redemption", 
    "Madagascar", "Memento Mori"
]

movies_starting_with_m = ...

# Output the result
print(movies_starting_with_m)
```

4. Use a list comprehension to select all movies that start with the letter 'M' and have a rating of 8.0 or higher.
```python
movies = [
    ("The Matrix", 8.7), ("Mad Max: Fury Road", 8.1), ("Memento", 8.4), 
    ("The Godfather", 9.2), ("Moonlight", 7.4), ("Inception", 8.8), 
    ("Manchester by the Sea", 7.8), ("Gladiator", 8.5), ("Mulan", 7.6), 
    ("Pulp Fiction", 8.9), ("Minari", 7.5), ("The Dark Knight", 9.0), 
    ("Moulin Rouge!", 7.6), ("Interstellar", 8.6), ("Monsters, Inc.", 8.1), 
    ("Titanic", 7.9), ("Murder on the Orient Express", 7.3), 
    ("The Shawshank Redemption", 9.3), ("Madagascar", 6.9), 
    ("Memento Mori", 8.3)
]

highly_rated_movies_starting_with_m = ...

# Output the result
print(highly_rated_movies_starting_with_m)
```

5. Write a function that takes two lists and returns a set of unique elements that are present in both lists.
 ```python
def common_elements(lst1, lst2):
    return ...

# Example usage
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: {3, 4}
```









