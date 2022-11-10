# Brute-force 0/1 Knapsack Problem Solution

def get_binary_rep(n, num_digits):
    """Assumes n and num_digits are non-negative ints
    Returns a str of length num_digits that is a binary representation of n"""

    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n//2

    if len(result) > num_digits:
        raise ValueError('not enough digits')
    for i in range(num_digits - len(result)):
        result = '0' + result
    return result

def gen_powerset(L):
    """Assumes L is a list
    Returns a list of lists that contains all possible
    combination of the elements of L. E.g., if L is [1, 2] it will return [], [1], [2], [1, 2]"""

    powerset = []
    for i in range(0, 2**len(L)):
        bin_str = get_binary_rep(i, len(L))
        subset = []
        for j in range(len(L)):
            if bin_str[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset


def choose_best(pset, max_weight, get_val, get_weight):
    best_val = 0.0
    best_set = None
    for items in pset:
        items_val = 0.0
        items_weight = 0.0
        for item in items:
            items_val += get_val(item)
            items_weight += get_weight(item)
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    return (best_set, best_val)

def test_best(max_weight = 20):
    items = build_items()

    pset = gen_powerset(items)
    taken, val = choose_best(pset, max_weight, Item.get_value, Item.get_weight)

    print(f"Total value of items taken is {val}")
    for item in taken:
        print(item)


test_best()