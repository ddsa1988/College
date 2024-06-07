import random


def bubble_sort(collection):
    if not isinstance(collection, list):
        return collection

    size = len(collection)

    for i in range(size):
        for j in range(size - i - 1):
            actual_item = collection[j]
            next_item = collection[j + 1]

            if actual_item > next_item:
                collection[j] = next_item
                collection[j + 1] = actual_item

    return collection


dataNumbers = random.sample(range(10), 10)
dataStrings = ["Rodrigo", "Zeus", "Diego", "Amanda"]

print(f"Before bubble sort: {dataNumbers}")
print(f"Before bubble sort: {dataStrings}")
print()

bubble_sort(dataNumbers)
bubble_sort(dataStrings)

print(f"After bubble sort: {dataNumbers}")
print(f"After bubble sort: {dataStrings}")
