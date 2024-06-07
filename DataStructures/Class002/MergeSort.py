def merge_sort(collection):
    if not isinstance(collection, list):
        return collection

    if len(collection) > 1:
        mid = int(len(collection) / 2)
        left = collection[0:mid]
        right = collection[mid:len(collection)]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                collection[k] = left[i]
                i += 1
            else:
                collection[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            collection[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            collection[k] = right[j]
            j += 1
            k += 1


dataNumbers = [54, 26, 93, 17, 77, 31, 44, 19, 55]

print(f"Before merge sort: {dataNumbers}")
merge_sort(dataNumbers)
print(f"After merge sort: {dataNumbers}")
