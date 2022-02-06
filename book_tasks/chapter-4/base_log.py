def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
        x > 1, epsilon > 0, power >= 1
        Returns float y such that base ** y is wtithin epsilon of x
    """
    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    # Perform bisection search
    ans = (low + high) / 2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
             low = ans
        else:
             high = ans
        ans = (low + high) / 2
    return ans
x = 8
base = 2
epsilon = 0.01
result = log(x, base, epsilon)

print(f"{result} is close to the log base {base} of {x}")