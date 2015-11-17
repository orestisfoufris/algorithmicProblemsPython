'''
Topcoder AddMultipy problem.
Problem statement: https://community.topcoder.com/stat?c=problem_statement&pm=13231&rd=15858&rm=&cr=23117867
'''

def makeExpression(y):
    for i in range(2, 1000):
        x2 = y - i * i
        if x2 >= -1000 and x2 <= 1000 and x2 is not 0 and x2 is not 1:
            return [i, i, x2]
