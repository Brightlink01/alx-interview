#!/usr/bin/python3
"""
  implemanting the depth first searching alg
"""


def minOperations(n: int) -> int:
    """
        calculates the fewest number of operations needed to result
    """

    if type(n) == int or n > 1:
        return int(ops(n))
    else:
        return 0


def ops(n: int) -> int:
    """ calculate n operations to copy paste"""
    op = 2
    sum = 0

    while n >= op:
        if n % op == 0:
            n = n // op
            sum += op
        else:
            op += 1
    return sum

