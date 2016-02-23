#-*- coding: utf-8 -*-

class IdentifyingWood:
    def check(self, s, t):
        i, j = 0, 0
        while i < len (s) and j < len (t):
            if s [i] == t [j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == len (t): return "Yep, it's wood."
        return "Nope."
