# Python Data Structures and C Linked List Palindrome

This project contains various Python functions for working with lists and tuples, as well as a C function to check if a singly linked list is a palindrome.

## Python Functions

0. `print_list_integer(my_list=[])`: Prints all integers of a list.
1. `element_at(my_list, idx)`: Retrieves an element from a list at a given index.
2. `replace_in_list(my_list, idx, element)`: Replaces an element of a list at a specific position.
3. `print_reversed_list_integer(my_list=[])`: Prints all integers of a list in reverse order.
4. `new_in_list(my_list, idx, element)`: Replaces an element in a list at a specific position without modifying the original list.
5. `no_c(my_string)`: Removes all characters 'c' and 'C' from a string.
6. `print_matrix_integer(matrix=[[]])`: Prints a matrix of integers.
7. `add_tuple(tuple_a=(), tuple_b=())`: Adds two tuples.
8. `multiple_returns(sentence)`: Returns a tuple with the length of a string and its first character.
9. `max_integer(my_list=[])`: Finds the biggest integer of a list.
10. `divisible_by_2(my_list=[])`: Finds all multiples of 2 in a list.
11. `delete_at(my_list=[], idx=0)`: Deletes the item at a specific position in a list.
12. `switch.py`: A script that switches the values of two variables.

## C Function

13. `is_palindrome(listint_t **head)`: Checks if a singly linked list is a palindrome.

### Compilation

To compile the C function, use the following command:

```
gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
```

### Usage

To use the Python functions, import them into your Python script. For example:

```python
from 0-print_list_integer import print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
```

To use the C function, include the `lists.h` header in your C file and call the `is_palindrome` function:

```c
#include "lists.h"

int main(void)
{
    listint_t *head = NULL;
    // Add nodes to the list
    int result = is_palindrome(&head);
    printf("Is palindrome: %d\n", result);
    return (0);
}
```