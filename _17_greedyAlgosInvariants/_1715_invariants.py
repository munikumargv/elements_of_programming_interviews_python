def has_two_sum(a, t):
    i, j = 0, len(a) - 1

    while i <= j:
        if a[i] + a[j] == t:
            return True
        elif a[i] + a[j] < t:
            i += 1
        else:   # a[i] + a[j] > t.
            j -= 1
    return False
