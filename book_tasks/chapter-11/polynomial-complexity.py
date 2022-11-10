# This function complexiy is O(len(L1) * len(L2))
def is_subset(L1, L2):
    """Assumes L1 and L2 are lists.
    Returns True if each element in L1 is alsi in L2 and False otherwise"""

    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False

    return True

#The complexity of this function is O(len(L1) * len(L2))

def intersect(L1, L2):
    """Assumes L1 and L2 are lists.
    Returns a list without duplicates that is the intersection of L1 and L2"""
    #Build a list containing common elements
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
                break
    #Build a list without duplicates
    result = []
    for e in tmp:
        if e not in result:
            result.append(e)
    return result