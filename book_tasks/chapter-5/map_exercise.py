def f(L1, L2):    
    """L1, L2 lists of same length of numbers    
    returns the sum of raising each element in L1    
    to the power of the element at the same index in L2    
    For example, f([1,2], [2,3]) returns 9"""
    
    if len(L1) != len(L2):
        return None

    return sum([L1[x]**L2[x] for x in range(len(L1))])

print(f([1,2], [2,3]))
print(f([1,2, 3], [2,3]))