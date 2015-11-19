'''
https://community.topcoder.com/stat?c=problem_statement&pm=13277
Method signature: int howManySquares(int[] sticks)
'''

def howManySquares(sticks):
    dictionary = {}
    for i in range(len(sticks)):
        if sticks[i] not in dictionary:
            dictionary[sticks[i]] = 1
        else:
            dictionary[sticks[i]] = dictionary[sticks[i]] + 1

    result = 0
    for k, v in dictionary.iteritems():
        result = result + (v / 4)

    return result

assert(howManySquares([1, 1, 2, 2, 1, 1, 2]) == 1)
assert(howManySquares([3, 1, 4, 4, 4, 10, 10, 10, 10]) == 1)
assert(howManySquares([1, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1]) == 2)
assert(howManySquares([2, 2, 4, 4, 8, 8]) == 0)
