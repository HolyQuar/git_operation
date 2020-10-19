"""Test construction is as simple as cutting-and-pasting
-a typical call
-along with its results into the docstring.
"""
# doctest
def average(values):
    """Compute the arithmetic mean of a list of numbers
    >>> print(average([20,30,70]))
    40.0
    """
    return sum(values)/len(values)
import doctest
doctest.testmod()

