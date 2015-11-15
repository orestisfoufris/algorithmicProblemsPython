"""
15-Nov-2015
https://community.topcoder.com/stat?c=problem_statement&pm=13160
Method signature:	int[] sort(String[] score, int x)
"""
import collections
import operator

def sort(scores, x):
    tuples = []
    for i in range(len(scores)):
        arr = list(scores[i])
        tuples.append((arr[x], i))

    tuples = sorted(tuples, key=operator.itemgetter(0))
    return [tuples[x][1] for x in range(len(tuples))]

assert(sort(["ACB", "BAC", "CBA"], 1) == [1, 2, 0])
assert(sort(["A", "C", "B", "C", "A"], 0) == [0, 4, 2, 1, 3])
assert(sort(["LAX","BUR","ONT","LGB","SAN","SNA","SFO","OAK","SJC"], 2) == [5, 3, 8, 7, 4, 6, 1, 2, 0])
assert(sort(["XXYWZWWYXZ","YZZZYWYZYW","ZYZZWZYYWW","ZWZWZWZXYW","ZYXWZXWYXY","YXXXZWXWXW","XWWYZWXYXY","XYYXYWYXWY","ZZYXZYZXYY","WXZXWYZWYY"], 3) == [0, 3, 4, 5, 7, 8, 9, 6, 1, 2])
assert(sort(["X"], 0) == [0])
