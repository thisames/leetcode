# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(5)
node7 = ListNode(5)
node8 = ListNode(5)
node9 = ListNode(5)

# Ligando os nós
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9


def deleteDuplicates(head: Optional[ListNode]):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    if head is None:
        return head

    original = head

    while head.next is not None:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next

    return original


head = [1, 1, 2, 3, 3]
head = [1, 2, 3, 3]
head = [1, 2, 3, 4]

print(deleteDuplicates(node1))
