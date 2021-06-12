a1 = 'ABCBABCBDAB'
a2 = 'ABCDABCDEFA'


def length_of_longest_substr(s):
    checklist = {}
    start = 0
    max_l = 0
    for i, v in enumerate(s):
        if v in checklist:
            if checklist[v] >= start:
                start = checklist[v] + 1

        current_l = i - start
        max_l = max(current_l, max_l)
        checklist[v] = i

    return max_l
