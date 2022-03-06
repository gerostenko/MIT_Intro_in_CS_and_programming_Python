def find_extreme_divisors(n1, n2):
    """ Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and
    the largest common divisor of n1 & n2. If not common divisor,
    other than 1, returns (None, None)"""
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if min_val == None:
                min_val = i
            else:
                max_val = i
    return min_val, max_val

min_divisor, max_divisor = find_extreme_divisors(100, 200)
print(f"minimum and maximum divisors of 100 and 200 respectively are {min_divisor} and {max_divisor}")