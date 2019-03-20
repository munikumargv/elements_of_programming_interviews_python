def matrix_search(a, x):
    row, col = 0, len(a[0]) - 1  # start from the top-right corner.
    # keeps searching while there are unclassified rows and columns
    while row < len(a) and col >= 0:
        if a[row][col] == x:
            return True
        elif a[row][col] < x:
            row += 1    # eliminate the row
        else:   # a[row][col] > x.
            col -= 1    # eliminate this column.
    return False
