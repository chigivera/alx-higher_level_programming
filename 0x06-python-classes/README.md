# Python Classes Project

This project is part of the ALX Higher Level Programming curriculum. It focuses on Object-Oriented Programming (OOP) in Python, specifically on creating and working with classes.

## Project Description

In this project, we implement a `Square` class with various features, gradually building up its functionality through a series of tasks. The project covers key OOP concepts such as class attributes, methods, property decorators, and encapsulation.

## Files in this Project

1. `0-square.py`: Defines an empty `Square` class.
2. `1-square.py`: Adds a private instance attribute `size` to the `Square` class.
3. `2-square.py`: Adds size validation to the `Square` class.
4. `3-square.py`: Adds a public instance method `area()` to calculate the square area.
5. `4-square.py`: Adds getter and setter methods for the `size` attribute.
6. `5-square.py`: Adds a public instance method `my_print()` to print the square.
7. `6-square.py`: Adds a private instance attribute `position` to the `Square` class.

## Tasks

### 0. My first square
- Create an empty class `Square` that defines a square.
- You are not allowed to import any module.

### 1. Square with size
- Add a private instance attribute `size` to the `Square` class.
- Instantiate with `size` (no type/value verification).

### 2. Size validation
- Add size validation to the `Square` class.
- `size` must be an integer, otherwise raise a `TypeError` exception.
- If `size` is less than 0, raise a `ValueError` exception.

### 3. Area of a square
- Add a public instance method `def area(self):` that returns the current square area.

### 4. Access and update private attribute
- Add property `def size(self):` to retrieve the private instance attribute `size`.
- Add property setter `def size(self, value):` to set `size`.

### 5. Printing a square
- Add a public instance method `def my_print(self):` that prints the square with the character `#`.
- If `size` is equal to 0, print an empty line.

### 6. Coordinates of a square
- Add a private instance attribute `position`.
- Add property `def position(self):` to retrieve `position`.
- Add property setter `def position(self, value):` to set `position`.
- Instantiate with optional `size` and optional `position`.
- If `position` is not a tuple of 2 positive integers, raise a `TypeError` exception.

## How to Use

Each file can be executed independently to test its functionality. For example:

```bash
./0-main.py
./1-main.py
# ... and so on
```

Make sure you have the necessary permissions to execute the files.

## Author

Ayman Benchamkha

## Acknowledgements

This project is part of the ALX Software Engineering curriculum.