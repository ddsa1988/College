# Big-O Quick Sort is O(n²).
def quick_sort(data, start, end):
    if start < end:
        partition_position = partition(data, start, end)
        quick_sort(data, start, partition_position - 1)
        quick_sort(data, partition_position + 1, end)


def partition(data, start, end):
    pivot = data[start]
    left = start + 1
    right = end
    flag = False

    while not flag:
        while left <= right and data[left] <= pivot:
            left += 1
        while right >= left and data[right] >= pivot:
            right -= 1
        if right < left:
            flag = True
        else:
            data[left], data[right] = data[right], data[left]

    data[start], data[right] = data[right], data[start]

    return right


dataNumbers = [54, 26, 93, 17, 77, 31, 44, 19, 55]

print(f"Before quick sort: {dataNumbers}")
quick_sort(dataNumbers, 0, len(dataNumbers) - 1)
print(f"After quick sort: {dataNumbers}")
