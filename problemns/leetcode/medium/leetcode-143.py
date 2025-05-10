# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


def get_middle(head):
    current = head
    size = 0
    while current:
        size += 1
        current = current.next

    current = head
    i = 0
    while i != (size // 2):
        current = current.next
        i += 1
    return current, size


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    mid, size = get_middle(head)

    while mid.next:
        current = head
        next_head = head.next
        current_mid = mid
        while current_mid.next.next != None:
            current_mid = current_mid.next

        current.next = current_mid.next
        head = next_head
        current_mid.next.next = head
        current_mid.next = None


head_data = [1, 2, 3, 4]
head = ListNode(head_data[0])
current = head

for i in range(1, len(head_data)):
    new_node = ListNode(head_data[i])
    current.next = new_node
    current = new_node

current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

reorderList(head)

current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
