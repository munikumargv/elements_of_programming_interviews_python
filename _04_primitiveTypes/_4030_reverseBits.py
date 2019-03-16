# Write a program that takes a 64-bit word and returns the 64-bit word consisting
# of the bits of the input word in reverse order.
def reverse_bits(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return(PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE) |
           PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) |
           PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] <<
           MASK_SIZE | PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK])
