# Fibonacci Sequence Function using Dynamic Programming

def fib_memo(n, memo = None):
    """Assumes n is an int >= 0, memo used only by recursive calls
    Returns Fibonacci of n"""
    if memo == None:
        memo = {}
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        memo[n] = result
        return result

def fib_tab(n):
    """Assumes n is an int >= 0
    Returns Fibonacci of n"""
    tab = [1]*(n+1) #only first two values matter
    for i in range(2, n+1):
        tab[i] = tab[i-1]+tab[i-2]
    return tab[n]

print(f"Result of Fibonacci sequence of 120 using fib_memo is {fib_memo(120)}")
print(f"Result of Fibonacci sequence of 120 using fib_tab is {fib_tab(120)}")