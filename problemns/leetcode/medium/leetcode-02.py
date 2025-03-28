# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_item(head, value):
    new_node = ListNode(value)

    if head is None:
        head = new_node
        return head

    current = head

    while current.next:
        current = current.next

    current.next = new_node

    return head


def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    number_str = ""
    while l1.next:
        number_str += str(l1.val)
        l1 = l1.next
    number_str += str(l1.val)

    number_str_two = ""
    while l2.next:
        number_str_two += str(l2.val)
        l2 = l2.next
    number_str_two += str(l2.val)

    sum = str(int(number_str[::-1]) + int(number_str_two[::-1]))

    sum_linkedlist = None

    for i in reversed(sum):
        sum_linkedlist = add_item(sum_linkedlist, i)

    return sum_linkedlist


node1_l1 = ListNode(2)
node2_l1 = ListNode(4)
node3_l1 = ListNode(3)

node1_l1.next = node2_l1
node2_l1.next = node3_l1

node1_l2 = ListNode(5)
node2_l2 = ListNode(6)
node3_l2 = ListNode(4)

node1_l2.next = node2_l2
node2_l2.next = node3_l2

addTwoNumbers(node1_l1, node1_l2)
