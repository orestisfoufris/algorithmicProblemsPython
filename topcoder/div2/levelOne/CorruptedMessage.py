import string

'''
Problem statement: https://community.topcoder.com/stat?c=problem_statement&pm=13748
Method Signature: String reconstructMessage(String s, int k)
'''

def reconstructMessage(s, k):
    if k == 0:
        return s

    set_alphabet = set(string.ascii_lowercase)
    set_word = set(s)

    len_s = len(s)

    letter = None
    for i in range(len_s):
        occ = 0
        for j in range(len_s):
            if s[i] == s[j]:
                occ += 1
        if len_s - occ == k:
            letter = s[i]

    if letter is None:
        for letter in set_alphabet:
            if letter not in set_word:
                return letter * k

    return letter * len_s
