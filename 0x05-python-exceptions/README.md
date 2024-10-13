# Python Exceptions Project

This project contains a series of Python scripts that demonstrate various exception handling techniques and safe operations.

## Files and Descriptions

1. `0-safe_print_list.py`
   - Contains the `safe_print_list` function.
   - Safely prints a specified number of elements from a list.

2. `1-safe_print_integer.py`
   - Contains the `safe_print_integer` function.
   - Safely prints an integer using "{:d}".format().

3. `2-safe_print_list_integers.py`
   - Contains the `safe_print_list_integers` function.
   - Prints the first x elements of a list that are integers.

4. `3-safe_print_division.py`
   - Contains the `safe_print_division` function.
   - Divides two integers and prints the result.

5. `4-list_division.py`
   - Contains the `list_division` function.
   - Divides two lists element by element.

6. `5-raise_exception.py`
   - Contains the `raise_exception` function.
   - Raises a TypeError exception.

7. `6-raise_exception_msg.py`
   - Contains the `raise_exception_msg` function.
   - Raises a NameError exception with a message.

## Usage

Each file contains a single function that can be imported and used in your Python scripts. For example:

```python
from 0-safe_print_list import safe_print_list

my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
```

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Your code should use the pycodestyle (version 2.8.*) style guide
- All your files must be executable
- The length of your files will be tested using `wc`

## Author

Ayman Benchamkha

## Project Status

This project is part of the ALX Higher Level Programming curriculum.