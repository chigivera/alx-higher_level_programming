#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    result = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result.append(div)
    return result
