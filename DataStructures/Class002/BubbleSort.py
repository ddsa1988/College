import random


# Big-O Bubble Sort is O(n²).
def bubble_sort(data):
    if not isinstance(data, list):
        return data

    size = len(data)

    for i in range(size):
        is_sorted = True
        for j in range(size - i - 1):
            actual_item = data[j]
            next_item = data[j + 1]

            if actual_item > next_item:
                data[j] = next_item
                data[j + 1] = actual_item
                is_sorted = False

        if is_sorted:
            break

    return data


data_numbers = random.sample(range(10), 10)
data_strings = ["Rodrigo", "Zeus", "Diego", "Amanda"]

print(f"Before bubble sort: {data_numbers}")
print(f"Before bubble sort: {data_strings}")
print()

bubble_sort(data_numbers)
bubble_sort(data_strings)

print(f"After bubble sort: {data_numbers}")
print(f"After bubble sort: {data_strings}")
