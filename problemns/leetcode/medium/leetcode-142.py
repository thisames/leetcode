from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Node:
    def __init__(self, ant, val, next):
        self.ant = ant
        self.val = val
        self.next = next


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    current = head
    node_list = []
    first = True
    ant = None
    while current:
        if first:
            ant = None
            val = current.val
            next = current.next.val
            new_node = Node(ant, val, next)
            node_list.append(new_node)
            ant = current.val
            current = current.next
            first = False
        for node in node_list:
            if current.next.val == node.val and current.next.next.val == node.next:
                return current.next
        val = current.val
        next = current.next.val
        new_node = Node(ant, val, next)
        node_list.append(new_node)
        ant = current.val
        current = current.next


def detectCycleRefactor(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    ptr = head
    while ptr != head:
        ptr = ptr.next
        slow = slow.next
    return ptr


node1_l1 = ListNode(3)
node2_l1 = ListNode(2)
node3_l1 = ListNode(0)
node4_l1 = ListNode(-4)

node1_l1.next = node2_l1
node2_l1.next = node3_l1
node3_l1.next = node4_l1
node4_l1.next = node2_l1

a = detectCycleRefactor(node1_l1)
print(a.val)
