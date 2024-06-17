import random


# Big-O Binary Search is O(log n).
def binary_search(data, item):
    if not isinstance(data, list):
        return -1

    data.sort()

    start = 0
    end = len(data) - 1

    while start <= end:
        mid = int((start + end) / 2)

        if not isinstance(item, type(data[mid])):
            break
        elif item > data[mid]:
            start = mid + 1
        elif item < data[mid]:
            end = mid - 1
        else:
            return mid

    return -1


data_numbers = random.sample(range(10), 10)
data_strings = ["Amanda", "Diego", "Rodrigo", "Zeus"]

print(binary_search(data_numbers, 6))
print(binary_search(data_strings, "Zeus"))
print(binary_search(data_strings, "Diego"))
