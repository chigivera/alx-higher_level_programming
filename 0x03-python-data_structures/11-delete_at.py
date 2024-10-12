def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.
    
    Args:
        my_list (list): The original list.
        idx (int): The index of the item to delete.
    
    Returns:
        The modified list if idx is valid, otherwise the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
