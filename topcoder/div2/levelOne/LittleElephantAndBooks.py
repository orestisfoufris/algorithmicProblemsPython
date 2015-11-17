'''
Topcoder LittleElephantAndBooks problem.
http://community.topcoder.com/stat?c=problem_statement&pm=12112
'''

def getNumber(pages, number):
    pages.sort()
    element = pages[number]
    pages = pages[:number-1]

    return sum(pages) + element
