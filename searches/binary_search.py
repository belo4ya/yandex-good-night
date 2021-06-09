import bisect


def binary_search(sorted_collection, item):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None


def bisect_binary_search(sorted_collection, item):
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return None


def recursion_binary_search(sorted_collection, item, left, right):
    if right < left:
        return None

    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return recursion_binary_search(sorted_collection, item, left, midpoint - 1)
    else:
        return recursion_binary_search(sorted_collection, item, midpoint + 1, right)
