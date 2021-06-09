import sys
from collections import Counter


def are_anagrams(string_1, string_2):
    if len(string_1) != len(string_2):
        return 0
    else:
        print(int(Counter(string_1) == Counter(string_2)))


first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

are_anagrams(first, second)
