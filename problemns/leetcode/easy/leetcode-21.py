from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def add_item(self, head, value):
        item = ListNode(value)

        if head is None:
            head = item
            return head

        current = head

        while current.next:
            current = current.next

        current.next = item
        return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list = []

        newlist = None

        while list1 and list1.next:
            list.append(list1.val)
            list1 = list1.next

        if list1:
            list.append(list1.val)

        while list2 and list2.next:
            list.append(list2.val)
            list2 = list2.next

        if list2:
            list.append(list2.val)

        list = sorted(list)

        for i in list:
            newlist = self.add_item(newlist, i)

        return newlist
