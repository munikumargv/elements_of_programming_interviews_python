def bst_in_sorted_order(tree):
    s, result = [], []

    while s or tree:
        if tree:
            s.append(tree)
            # going left
            tree = tree.left
        else:
            # going up
            tree = s.pop()
            result.append(tree.data)
            # going right
            tree = tree.right
    return result