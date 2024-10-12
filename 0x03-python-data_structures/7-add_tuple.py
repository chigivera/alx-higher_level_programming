#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples.
    
    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.
    
    Returns:
        A tuple with the sum of the corresponding elements of tuple_a and tuple_b.
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
