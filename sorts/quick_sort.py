def quick_sort(collection: list) -> list:
    if len(collection) < 2:
        return collection
    pivot = collection.pop()
    greater = []
    lesser = []
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
