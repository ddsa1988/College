def hash_func_number(key, size):
    if not (isinstance(key, int) or isinstance(key, float)) and isinstance(size, int):
        return -1

    if key < 0 or size < 1:
        return -1

    return key % size


def hash_func_digits(key, size):
    pass
