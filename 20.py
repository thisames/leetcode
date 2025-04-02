from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def count_size_list(self, head: ListNode) -> int:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def add_item(self, head, value):
        new_node = ListNode(value)

        if head is None:
            head = new_node
            return head

        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head

    def get_half_list_left(self, head, index):
        left_list = None

        count = 0
        current = head
        while current.next:
            if count == index:
                break
            left_list = self.add_item(left_list, current.val)
            count += 1
            current = current.next

        return left_list

    def get_half_list_right(self, head, index):
        right_list = None

        count = 0
        current = head
        while current.next:
            if count >= index:
                right_list = self.add_item(right_list, current.val)
            count += 1
            current = current.next

        right_list = self.add_item(right_list, current.val)

        return right_list

    def merge_sorting_linked(self, head: ListNode) -> ListNode | None:
        if head and head.next is None:
            return head

        if head is None:
            return head

        list_size = self.count_size_list(head)
        mid = list_size // 2
        left = self.merge_sorting_linked(self.get_half_list_left(head, mid))
        right = self.merge_sorting_linked(self.get_half_list_right(head, mid))

        return self.merge_linked(left, right)

    def merge_linked(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        current.next = left if left else right

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sorting_linked(head)
