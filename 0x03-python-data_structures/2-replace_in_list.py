def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.
    
    Args:
        my_list (list): The original list.
        idx (int): The index of the element to replace.
        element: The new element to insert.
    
    Returns:
        The modified list if idx is valid, otherwise the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
