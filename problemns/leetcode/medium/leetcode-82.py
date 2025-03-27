from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_item(head, value):
    new_node = ListNode(value)

    current_storage = head
    while current_storage.next:
        current_storage = current_storage.next

    current_storage.next = new_node

    return head


"""
well, thats my first medium question in leetcode. I feel happy for got it
but the solution is very bad and not performance. I still have improved me a lot
"""


def deleteDuplicates(head: Optional[ListNode]):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if head and head.next is None:
        return head

    if head is None:
        return head

    first = True

    list = []
    while head.next is not None:
        prev = head
        current = head.next
        prox = None

        if head.next.next is not None:
            prox = head.next.next.val

        if first:
            if current.val != prev.val:
                list.append(prev.val)
            first = False

        if current.val != prev.val and current.val != prox:
            list.append(current.val)

        head = head.next
    if len(list) > 0:
        linkedlist = ListNode(list[0])
        for i in range(1, len(list)):
            add_item(linkedlist, list[i])
        return linkedlist
    return None


node1 = ListNode(1)

# node3 = ListNode(3)
# node4 = ListNode(3)
# node5 = ListNode(4)
# node6 = ListNode(4)
# node7 = ListNode(5)
# node8 = ListNode(7)
# node9 = ListNode(9)

# Ligando os nós


# node3.next = node4
# node4.next = node5
# node5.next = node6
# node6.next = node7


# node7.next = node8
# node8.next = node9


print(deleteDuplicates(node1))
