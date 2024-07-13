"""
变位词判断
"""

def anagramSolution(s1, s2):
    letter_dict = {}

    for c1, c2 in zip(s1, s2):
        letter_dict.setdefault(c1, 0)
        letter_dict.setdefault(c2, 0)
        letter_dict[c1] += 1
        letter_dict[c2] -= 1

    return not any(val for val in letter_dict.values())


print(anagramSolution('aacde', 'cadae'))
