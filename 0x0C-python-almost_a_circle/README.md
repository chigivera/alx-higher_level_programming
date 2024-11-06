# Python - Almost a Circle

This project is a review of Python concepts through the implementation of a Base class and its subclasses Rectangle and Square. It covers:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file
- args and kwargs
- Serialization/Deserialization
- JSON

## Project Structure

### Models
- `models/base.py`: The base class of all other classes in the project
- `models/rectangle.py`: Rectangle class that inherits from Base
- `models/square.py`: Square class that inherits from Rectangle

### Tests
- `tests/test_models/test_base.py`: Unit tests for Base class
- `tests/test_models/test_rectangle.py`: Unit tests for Rectangle class
- `tests/test_models/test_square.py`: Unit tests for Square class

### Main Files
Test files for each task:
- 0-main.py through 18-main.py: Basic test files
- 100-main.py: Advanced task for CSV serialization
- 101-main.py: Advanced task for drawing shapes

## Requirements
- Python 3.8.5
- pycodestyle 2.8.*
- Unittest module

## File Descriptions

### Base Class (`models/base.py`)
The base class for all other classes in the project. Contains:
- Private class attribute `__nb_objects`
- Class constructor `__init__`
- Static methods for JSON string conversion
- Class methods for file handling
- Methods for instance creation and drawing

### Rectangle Class (`models/rectangle.py`)
Inherits from Base and adds:
- Private instance attributes with getters/setters
- Class constructor
- Area calculation
- Display method
- String representation
- Update method
- Dictionary representation

### Square Class (`models/square.py`)
Inherits from Rectangle and adds:
- Size getter/setter
- String representation
- Update method
- Dictionary representation

## Testing
All files, classes and methods are unit tested with the unittest module.
Tests can be executed by running:
```bash
python3 -m unittest discover tests
Authors
[Ayman Benchamkha]

License
This project is licensed under the terms of the MIT license.



This README provides a comprehensive overview of the project structure, requirements, and file descriptions. Make sure to replace "[Your Name]" with your actual name in the Authors section.

The file structure follows the project requirements and includes all necessary files for both mandatory and advanced tasks. Each file will need to be populated with the appropriate code based on the task requirements.

Would you like me to provide the content for any specific file?