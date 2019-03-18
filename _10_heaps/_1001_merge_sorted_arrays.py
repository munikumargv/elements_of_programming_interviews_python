import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    # builds a list of iterators for each array in sorted_arrays
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # puts first element from each iterator in min_heap
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result


# pythonic solution, uses the heapq.merge() method which takes multiple inputs.
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))
