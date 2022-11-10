#The complexity of this function is O(len(s))
def add_digits(s):
    """Assumes s is a string
    Returns the sum of the digits in n"""

    val = 0
    for c in s:
        val += int(c)
    return val

# Linear complexity does not always imply looping. It might occur with recursion as well
# The complexity of this function is O(x)

def factorial(x):
    """ Assumes that x is an a positive int
    Returns x!"""

    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    