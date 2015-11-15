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
