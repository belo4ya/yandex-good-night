class _Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"node({self.data})"

    __str__ = __repr__


class LinkedList:

    def __init__(self):
        self.start = None

    def insert(self, index: int, data):
        node = _Node(data)
        if self.start is None:
            self.start = node
        elif index == 0:
            node.next = self.start
            self.start = node
        else:
            current = self.start
            for _ in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

    def prepend(self, data):
        self.insert(0, data)

    def append(self, data):
        self.insert(len(self), data)

    @staticmethod
    def from_string(s: str):
        new_linked = LinkedList()
        for ch in list(s):
            new_linked.append(ch)
        return new_linked

    def __len__(self) -> int:
        return len(list(iter(self)))

    def __iter__(self):
        node = self.start
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        return " > ".join([str(item) for item in self])

    __str__ = __repr__


def remove_same_head(s: str, same: list[str]) -> LinkedList:
    from_string = LinkedList.from_string(s[::-1])  # предварительно развернем строку
    without_vowels = LinkedList()

    for el in from_string:
        if el not in same:
            without_vowels.prepend(el)  # O(1)

    return without_vowels


def remove_same_tail(s: str, same: list[str]) -> LinkedList:
    from_string = LinkedList.from_string(s)
    without_vowels = LinkedList()

    for el in from_string:
        if el not in same:
            without_vowels.append(el)  # O(n)

    return without_vowels


if __name__ == '__main__':
    from string import ascii_letters
    import time

    vowels = ['a', 'e', 'i', 'u', 'y', 'o', 'A', 'E', 'I', 'U', 'Y', 'O']
    string = (ascii_letters * 800)

    start = time.process_time()
    remove_same_head(string, vowels)
    print(f"prepend with reverse: {time.process_time() - start}")  # 18.5625

    start = time.process_time()
    remove_same_tail(string, vowels)
    print(f"append: {time.process_time() - start}")  # 31.4375
