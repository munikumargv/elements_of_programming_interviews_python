from _07_linkedLists._7000_listNode import ListNode


def merge_two_sorted_lists(l1, l2):
    # creates a placeholder for the result
    dummy_head = tail = ListNode()

    while l1 and l2:
        if l1.data < l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next

    # appends the remaining nodes of l1 or l2
    tail.next = l1 or l2
    return dummy_head.next
