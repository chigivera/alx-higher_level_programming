# Python - Test-driven development

This project contains Python scripts that demonstrate test-driven development practices. Each script is accompanied by its corresponding test file.

## Files

1. `0-add_integer.py`: A function that adds two integers.
   - Corresponding test file: `tests/0-add_integer.txt`

2. `2-matrix_divided.py`: A function that divides all elements of a matrix.
   - Corresponding test file: `tests/2-matrix_divided.txt`

3. `3-say_my_name.py`: A function that prints a name.
   - Corresponding test file: `tests/3-say_my_name.txt`

4. `4-print_square.py`: A function that prints a square using the `#` character.
   - Corresponding test file: `tests/4-print_square.txt`

5. `5-text_indentation.py`: A function that adds two new lines after `.`, `?`, and `:` characters in a text.
   - Corresponding test file: `tests/5-text_indentation.txt`

6. `6-max_integer.py`: A function that finds the maximum integer in a list.
   - Corresponding test file: `tests/6-max_integer_test.py`

## Usage

To run the tests for each file, use the following command:

```
python3 -m doctest -v ./tests/[test_file_name]
```

For the `6-max_integer_test.py`, use:

```
python3 -m unittest tests.6-max_integer_test
```

## Style

All Python scripts follow the PEP 8 style guide and have been checked with `pycodestyle`.

## Author

Ayman Benchamkha