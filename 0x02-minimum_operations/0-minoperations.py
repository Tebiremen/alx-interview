#!/usr/bin/python3
"""
In a text file, there is a single character H.
The Minimum Operations task.
"""


def minOperations(n):
    """
    Put in the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
