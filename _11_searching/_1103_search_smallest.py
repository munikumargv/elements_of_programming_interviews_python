def search_smallest(a):
    left, right = 0, len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if a[mid] > a[right]:
            # minimum must be in a[mid + 1:right + 1].
            left = mid + 1
        else:   # a[mid] < a[right].
            # minimum cannot be in a[mid + 1:right + 1] so it must be in a[
            # left:mid + 1].
            right = mid
    # loop ends when left == right
    return left
