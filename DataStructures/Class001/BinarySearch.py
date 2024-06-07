import random


def binary_search(collection, item):
    if not isinstance(collection, list):
        return -1

    collection.sort()

    start = 0
    end = len(collection)

    while start <= end:
        mid = int((start + end) / 2)

        if not isinstance(item, type(collection[mid])):
            break
        elif item > collection[mid]:
            start = mid + 1
        elif item < collection[mid]:
            end = mid - 1
        else:
            return mid

    return -1


dataNumbers = random.sample(range(10), 10)
dataStrings = ["Amanda", "Diego", "Rodrigo", "Zeus"]

print(binary_search(dataNumbers, 6))
print(binary_search(dataStrings, "Zeus"))
print(binary_search(dataStrings, "Diego"))
