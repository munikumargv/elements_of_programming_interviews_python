def search_entry_equal_to_its_index(a):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        difference = a[mid] - mid
        # a[mid] == mid if and only if difference == 0.
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        else:   # difference < 0.
            left = mid + 1
    return -1
