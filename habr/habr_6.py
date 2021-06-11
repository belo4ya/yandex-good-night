# Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
#
# Т.е. сгруппировать слова по "общим буквам".
from collections import defaultdict


def group_words(words):

    groups = defaultdict(list)

    for word in words:  # O(n)
        key = ''.join(sorted(word))
        groups[key].append(word)

    return [sorted(words) for words in groups.values()]  # O(n*log(n))


print(group_words(["eat", "tea", "tan", "ate", "nat", "bat"]))
