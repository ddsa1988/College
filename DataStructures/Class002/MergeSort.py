# Big-O Merge Sort is O(n.log n).
def merge_sort(data):
    if not isinstance(data, list):
        return data

    if len(data) > 1:
        mid = int(len(data) / 2)
        left = data[0:mid]
        right = data[mid:len(data)]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


dataNumbers = [54, 26, 93, 17, 77, 31, 44, 19, 55]

print(f"Before merge sort: {dataNumbers}")
merge_sort(dataNumbers)
print(f"After merge sort: {dataNumbers}")
