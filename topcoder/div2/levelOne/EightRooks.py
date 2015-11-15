"""
EightRooks problem
link: http://community.topcoder.com/stat?c=problem_statement&pm=13773&rd=16417
editorial: http://apps.topcoder.com/wiki/display/tc/SRM+657

"""

def isCorrect(board):
    dict = {}
    for i in board:
        letters = list(i)
        if letters.count("R") > 1:
            return "Incorrect"

        for j in letters:
            if j == "R":
                dict[letters.index(j)] = j

    if len(dict) == 8:
        return "Correct"

    return "Incorrect"
