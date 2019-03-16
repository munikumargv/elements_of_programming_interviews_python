from _07_linkedLists._7000_listNode import ListNode


# assumes L has at least k nodes, deletes the k-th last node in L
def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to the (k + 1)-th last node, deletes its successor
    second.next = second.next.next
    return dummy_head.next