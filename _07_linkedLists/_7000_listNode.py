class ListNode:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


# search for a key
def search_list(linkedlist, key):
    while linkedlist and linkedlist.data != key:
        linkedlist = linkedlist.next
    # if key was not present in the list, L will have become null
    return linkedlist


# insert a new node after a specified node
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


# delete the node past this one. assume node is not a tail.
def delete_after(node):
    node.next = node.next.next


# https://www.youtube.com/watch?v=JlMyYuY1aXU
class LinkedList:

    def __init__(self):
        self.head = ListNode()

    def append(self, data):
        new_node = ListNode(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next is not None:
            total += 1
            curr = curr.next
        return total

    def display(self):
        elements = []
        curr_node = self.head
        while curr_node is not None:
            curr_node = curr_node.next
            elements.append(curr_node.data)
        print(elements)
