#This function complexity is O(len(L)*len(L)) =  O(len(L)^2)
def sel_sort(L):
    """Assumes that L is a list of elements that can be compared using >
    Sorts L in ascending order"""
    suffix_start = 0
    while suffix_start != len(L):
        #look at each element in suffix
        for i in range(suffix_start, len(L)):
            if L[i] < L[suffix_start]:
                #swap position of elements
                L[suffix_start], L[i] = L[i], L[suffix_start]
        suffix_start += 1

def merge(left, right, compare):
    """Assumes left and right are sorted lists and compare defines an ordering on the elements.
    Returns a new sorted (by compare) list containing the same elements as (left + right) would contain."""

    result = []
    i, i = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

#This function compelxity is O(log(len(L)))
def merge_sort(L, compare = lambda x, y: x < y):
    """Assumes L is a list, compare defines an odering of elements of L"""

    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)





