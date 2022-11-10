
# Finger exercise below:
#First option, kinda greedy
# def make_change_greedy(coin_vals, change):
#     """coin_vals is a list of positive ints and coin_vals[0] = 1
#     change is a positive int
#     Return the minimum number of coins needed to have a set of coins the values of which sum to change.
#     Coins may be used more than once.
#     For example, make_change([1,5,8],11) should return 3."""
#     coin_vals.sort(reverse=True)


#     def make_change_recursive(vals, goal):
#         for val in vals:
#             whole_num = goal // val # how many times a current number needs to be divided to be the closest possible to change
#             remainder = goal % val # how much left to be summed to get to change

#             if remainder == 0:
#                 return whole_num
#             elif remainder == 1:
#                 return whole_num + 1
#             else:
#                 return whole_num + make_change_recursive([i for i in vals if i < remainder], remainder)

#     current = change
#     for i in range(len(coin_vals)):
#         coin = coin_vals[i]
#         result = make_change_recursive(coin_vals[i:], change)
#         if result < current:
#             current = result

#     return current


# print(make_change_greedy([1,5,8],11)) # should be 3
# print(make_change_greedy([1,5,8],13))# should be 2, but it's not, this is the flaw


#Version 2, fully working
def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1
    change is a positive int
    Return the minimum number of coins needed to have a set of coins the values of which sum to change.
    Coins may be used more than once.
    For example, make_change([1,5,8],11) should return 3."""

    sums_table = set(coin_vals)
    changes = 1 # starting with one because first iteration will always be two elements of the same list summed (so it's two coins)
    found = False

    while changes < change and found == False: # changes < change, because we know that 1 is always in the list, so change * 1 = change is maximum iterations needed in the worst case
        tmp_table = set()
        changes += 1
        for coin in coin_vals:
            for sum_val in sums_table:
                new_sum = coin + sum_val
                if new_sum == change:
                    found = True
                if new_sum > change:
                    continue
                tmp_table.add(new_sum)
        sums_table=set(tmp_table)
        tmp_table.clear()
    return changes


print(make_change([1,50,81],11)) # should be 11
print(make_change([1,5,8],11)) # should be 3
print(make_change([1,5,8],13))# should be 2
print(make_change([1,5,8,10],50))# should be 5
print(make_change([1,5,8,10],51))# should be 6