#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from a string.
    
    Args:
        my_string (str): The input string.
    
    Returns:
        A new string with all 'c' and 'C' characters removed.
    """
    return ''.join(char for char in my_string if char.lower() != 'c')