#Complexity of this function is O(log(i))
def int_to_str(i):
    """Assumes i is a non-negative int
    Returns a decimal string representation of i"""

    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result

#The complexity of this function is O(log(n))
def add_digits(n):
    """Assumes n is a non-negative int
    Returns the sum of the digits in n"""

    string_rep = int_to_str(n)
    val = 0
    for c in string_rep:
        val += int(c)
    return val
