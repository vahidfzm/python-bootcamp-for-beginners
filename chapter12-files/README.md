# Python For Beginners - Chapter 12 - Files

A file is a collection of data stored on a disk with a specific name and a directory path. File type can be text file or binary file. 

A binary file is a file that contains data in a format that is not human-readable. Image file, audio file, video file, etc. are examples of binary files.

A text file is a file that contains plain text without any formatting or special characters.


Python has a built-in function called `open()` that allows you to open a file. The open() function takes two arguments: the file name and the mode.
The mode specifies how you want to open the file. The most common modes are:
- "r" - Read - Default value. Opens a file for reading. If the file does not exist, it raises an error.
- "a" - Append - Opens a file for appending. If the file does not exist, it creates a new file.
- "w" - Write - Opens a file for writing. If the file exists, it truncates the file.
- "x" - Create - Creates the specified file. If the file already exists, the operation fails.
- "t" - Text - Default value. Opens the file in text mode.
- "b" - Binary - Opens the file in binary mode.

In addition to the mode, you can specify the encoding of the file. The default encoding is platform-dependent. You can specify the encoding using the encoding parameter.


1. Reading a file
```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```
with is a context manager that automatically closes the file when the block of code is executed.
the example above is equivalent to the following code:

```python
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

2. Create a new file and write to it
```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")
```


3. Append to an existing file
```python
with open("output.txt", "a") as file:
    file.write("This is an appended line.\n")
```




## File Operations:
In addition to reading and writing files, Python provides many other file operations, such as creating, deleting, renaming, copying, and moving files (modules like os, shutil, pathlib, etc.)

- Check if a file exists
```python
import os
if os.path.exists("filename"):
    print("File exists")
```

- Delete a file
```python
import os
os.remove("filename")
```




## File related variables
- __file__: The __file__ variable contains the path to the current file.
- __name__: The __name__ variable contains the name of the current module.



