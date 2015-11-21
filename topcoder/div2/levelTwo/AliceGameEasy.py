'''
Problem statement: https://community.topcoder.com/stat?c=problem_statement&pm=13524&rd=16082
Method signature: long findMinimumValue(long x, long y)
'''
import math

def findMinimumValue(x, y):
    turns = 0
    total_points = x + y
    while turns * (turns + 1) / 2 < total_points:
        turns += 1

    if turns * (turns + 1) / 2 > total_points:
        return -1

    result = 0
    while x > 0 and turns >= 0:
        if x >= turns:
            x -= turns
            result += 1
        turns -= 1

    if turns == -1:
        return -1

    return result


assert(findMinimumValue(10, 0) == 4)
assert(findMinimumValue(7, 14) == 2)
assert(findMinimumValue(5, 5) == 2)
assert(findMinimumValue(13, 15) == 2)
assert(findMinimumValue(5000, 50) == 91)
assert(findMinimumValue(932599670050, 67400241741) == 1047062)
