#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list.
    Args:
        my_list (list): The list of integers to print.
    """
    for num in my_list:
        print("{:d}".format(num))
