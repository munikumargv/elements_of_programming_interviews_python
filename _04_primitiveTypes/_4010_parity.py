"""
def parity(x):
    MASK_SIZE = 16
    BIT_MASK = 0XFFF
    return(PRECOMPUTED_PARITY[x >> 3 * MASK_SIZE] ^
           PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
           PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
           PRECOMPUTED_PARITY[x & BIT_MASK])
"""

class ParCheck:

    def __init__(self):
        pass

    def
