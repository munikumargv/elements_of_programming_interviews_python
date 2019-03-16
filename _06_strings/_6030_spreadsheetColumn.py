from functools import reduce


def ss_decode_col_id(col):
    return reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)
