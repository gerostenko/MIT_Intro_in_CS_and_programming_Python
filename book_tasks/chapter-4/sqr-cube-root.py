x1 = int(input("Enter number: "))
epsilon = 0.01
# Find square root of x1
if x1 < 0:
    print("Does not exist")
else:
    low = 0
    high = max(1, x1)
    ans = (high + low)/2
    while abs(ans**2 - x1) >= epsilon:
        if ans**2 < x1:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
x1_root = ans
x2 = -8
#Find cube root fo x2
if x2 < 0:
    is_pos = False
    x2 = -x2
else:
    is_pos = True
    
low = 0
high = max(1, x2)
ans = (high + low)/2
while abs(ans**3 - x2) >= epsilon:
    if ans**3 < x2:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
if is_pos:
    x2_root = ans
else:
    x2_root = -ans
    x2 = -x2
print(f"Sum of square root {x1}, and cube root of {x2} is close to {x1_root + x2_root}")



#The logic but more flexible using function
def find_root(num, power, epsilon):
    # Find interval containing answer
    if num < 0 and power%2 == 0:
        return None #Negative number has no even-powered roots
    low = min(-1, num)
    high = max(1, num)
    # Use bisection search
    ans = (high + low)/2
    while abs(ans**power - num) >= epsilon:
        if ans**power < num:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans
        
# Testing find_root
def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = "No root exists"
                else:
                    val = "Okay"
                    if abs(result**p -x) > e:
                        val = "Bad"
                    print(f"f'x = {x}, power = {p}, epsilon = {e}: {val} {result}")
x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)
test_find_root((x_vals), powers, epsilons)


epsion = 0.001
sqrt25 = find_root(25, 2, epsion)
cbrt_neg_8 = find_root(-8, 3, epsion)
fouth_rt_16 = find_root(16, 4, epsion)

print(f"The sum of suqre roots above is {sqrt25+cbrt_neg_8+fouth_rt_16}")
    