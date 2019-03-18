def search_first_of_k(a, k):
    left, right, result = 0, len(a) - 1, -1
    # a[left:right + 1] is the candidate set.
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > k:
            right = mid - 1
        elif a[mid] == k:
            result = mid
            right = mid - 1     # nothing to the right of mid can be solution.
        else:   # a[mid] < k
            left = mid + 1
    return result
