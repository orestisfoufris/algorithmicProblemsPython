"""
http://community.topcoder.com/stat?c=problem_statement&pm=14005&rd=16548
"""

def encrypt(message, key, K):
    msg_list = list(message)
    result = []
    while (K > 0):
        for i in key:
            result.insert(key[i], msg_list[i])
        K = K - 1
    return ''.join(result)

assert(encrypt("abc", [1,2,0], 1), "cab")
assert(encrypt("abcde", [4,3,2,1,0], 1), "edcba")
assert(encrypt("abcde", [4,3,2,1,0], 2), "abcde")
assert(encrypt("uogcodlk", [4,3,6,2,5,1,0,7], 44), "goodluck")
