'''
problem statement : https://community.topcoder.com/stat?c=problem_statement&pm=13072
mthod signature: int write(String word)
'''
import math

def write(word):
    word_list = list(word)
    count = 0
    for i in range(len(word_list)):
        count += abs(ord('A') - ord(word_list[i])) + 1

    return count

assert(write("ABC") == 6)
assert(write("TOPCODER") == 96)
assert(write("SINGLEROUNDMATCH") == 183)
assert(write("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ") == 1300)
