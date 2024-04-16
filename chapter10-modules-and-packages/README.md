# Python For Beginners - Chapter 10 - Modules and Packages

Module is a file containing Python code which can be imported into another file.

Package is a collection of modules in a directory.

## Built-in Modules
Python has a lot of built-in modules that you can use in your code to save time. 

Some of the most commonly used built-in modules are:

1. `math`: Provides mathematical functions.
2. `random`: Generates random numbers.
3. `os`: Provides a way to interact with the operating system.
4. `sys`: Provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
5. `datetime`: Provides classes for manipulating dates and times.


##  Importing Modules 
There are several ways to import a module in Python. 

```python
# import module_name
# import module_name as alias
# from module_name import function_name
# from module_name import *
# from package_name import module_name
# from package_name import module_name as alias
```
Examples:


```python
import math
print(math.pi)
```

```python
import math as m
print(m.pi)
```

```python
from math import pi
print(pi)
```

```python
from math import *
print(pi)
```

```python
from math import pi as p
print(p)
```



## Third-Party Modules
In addition to the built-in modules, Python has a vast ecosystem of third-party modules that you can use in your code.

You can install third-party modules using the `pip` command.

Python Package Index (PyPI) is a repository of third-party modules that you can install using `pip`.

Some of the most commonly used third-party modules are:
1. `requests`: Provides a way to send HTTP requests.
2. `beautifulsoup4`: Provides a way to parse HTML and XML documents.
3. `numpy`: Provides support for large, multi-dimensional arrays and matrices.
4. `pandas`: Provides data structures and data analysis tools.
5. `matplotlib`: Provides a way to plot graphs and charts.

### pip commands
to install a module using pip:
```python
pip install module_name
```

to uninstall a module using pip:
```python
pip uninstall module_name
```
to list all installed modules:
```python
pip list
```
to list all installed modules with version:
```python
pip freeze
```
to install a specific version of a module:
```python
pip install module_name==version
```
to upgrade a module to the latest version:
```python
pip install --upgrade module_name
```






