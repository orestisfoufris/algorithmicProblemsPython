'''
Topcoder problem div2 levelOne
'''
def construct(a):
    s = {4, 7, 44, 47, 74, 77}
    for i in range(a + 1, 101):
        result = a ^ i
        if result in s:
            return i
    return -1
