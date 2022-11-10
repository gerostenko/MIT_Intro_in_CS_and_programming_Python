#Linear search

def search(L, e):
    """Assumes L is a list, the elements of which are in ascending order.
    Returns True if e is in L, False otherwise."""

    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > i:
            return False
    return False

#Recursive binary search
# This function's complexity is O(log(len(L)))
def bin_search(L, e):
    """Assumes L is a list, the elements of which are in ascending order.
    Returns True if e is in L, False otherwise."""

    def bin_search_internal(L, e, low, high):
        #Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bin_search_internal(L, e, low, mid-1)
        else:
            return bin_search_internal(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bin_search_internal(L, e, 0, len(L) - 1)

