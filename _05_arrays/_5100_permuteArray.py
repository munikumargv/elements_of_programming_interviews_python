def apply_permutation(perm, a): # happens in O(n) time
    for i in range(len(a)):
        # check if the element at index i has not been moved by checking if
        # perm[i] is nonnegative
        next = i
        while perm[next] >= 0:
            a[i], a[perm[next]] = a[perm[next]], a[i]
            temp = perm[next]
            # subtracts len(perm) from an entry in perm to make it negative,
            # which indicates the corresponding move has been performed
            perm[next] -= len(perm)
            next = temp
    # restore perm
    perm[:] = [b + len(perm) for b in perm]


