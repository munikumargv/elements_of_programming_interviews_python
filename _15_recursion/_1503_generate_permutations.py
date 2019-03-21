def permutations(a):
    def directed_permutations(i):
        if i == len(a) - 1:
            result.append(a.copy())
            return

        # try every possibility for a[i].
        for j in range(i, len(a)):
            a[i], a[j] = a[j], a[i]
            # Generate all permutations for a[i + 1:].
            directed_permutations(i + 1)
            a[i], a[j] = a[j], a[i]

    result = []
    directed_permutations(0)
    return result
