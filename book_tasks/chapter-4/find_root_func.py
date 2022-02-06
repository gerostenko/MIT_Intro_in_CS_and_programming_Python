def find_root(x, power, epsilon):
    """Assumesx and epsilon int of float, power an int,
    epsilon > 0 & power >= 1
    Returns float y such that y**power is within epsilon of x.
    If such a float does not exist, it returns None"""
    if x < 0 and power%2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    ans = (low + high)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (low + high)/ 2
    return ans

print(find_root(4, 2, 0.01))