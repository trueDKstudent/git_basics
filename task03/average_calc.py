#!/usr/bin/env python3

""" This script shows functionality of custom
function that calculates average of input nubers
"""

def avg(num1, num2, *args):
    """Calculates average of set of numbers
    
    Calculates average of numbers returning their
    average

    Args:
        num1: first number
	num2: second number
 	*args: the rest of the numbers

    Returns:
	Average of num1, num2 and *args

    Arguments num1 and num2 are added as two separate
    positioned arguments in order to prevent calculation
    of less then two numbers since it does not make sence.
    """
    s = num1 + num2 + sum(args)
    l = 2 + len(args)
    return s / l

def main(args):

    av1 = avg(1, 2, 3, 4)
    av2 = avg(1, 2, *[3, 4])
    av3 = avg(*(1, 2, 3, 4))
    #help(avg)
    print(f'Average of positioned arguments only: {av1:}\n')
    print(f'Average of positioned and iterated arguments: {av2:}\n')
    print(f'Average of iterated arguments only: {av3:}\n')

if __name__ == '__main__':
    import sys

    main(sys.argv)
