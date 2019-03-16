def has_cycle(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # finds the start of the cycle
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            # both iterators advance in tandem
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it   # iter is the start of cycle
    return None     # no cycle


# TEST CODE: IS THIS RIGHT? (Book question)
def has_cycle_1(head):
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:    # there is a cycle
            # tries to find the start of the cycle
            slow = head
            # both pointers advance at the same time
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow     # slow is the start of the cycle
    return None     # no cycle
