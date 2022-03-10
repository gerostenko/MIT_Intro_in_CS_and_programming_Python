# The harmonic sum of an integer, n > 0, can becalculated using 
# the formula 1 + 1/2 + 1/3 + ... 1/n. 
# Write a recursive functionthat computes this.

def harmonic_sum_rec(n):
    if n == 1:
        return 1
    else:
        return harmonic_sum_rec(n-1) + 1/n
    
print(harmonic_sum_rec(10))
print(harmonic_sum_rec(11))