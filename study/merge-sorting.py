def merge_sort_iterative(arr):
    n = len(arr)
    width = 1

    while width < n:
        i = 0
        while i < n:
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
            i += 2 * width
        width *= 2

    return arr


def merge_sorting(arr, depth=0):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    right = merge_sorting(arr[mid:], depth + 1)
    left = merge_sorting(arr[:mid], depth + 1)

    print("  " * depth + f"right at depth {depth}: {right}")

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        print(i, j)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_half_list(head, index):
    right_list = None
    left_list = None
    left = True
    right = False

    count = 0
    current = head
    while current.next:
        if count == index:
            left = False
            right = True
        if left:
            left_list = add_item(left_list, current.val)
        if right:
            right_list = add_item(right_list, current.val)
        count += 1
        current = current.next

    return left_list, right_list


def count_size_list(head: ListNode) -> int:
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
    return count


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


def get_half_list_left(head, index):
    left_list = None

    count = 0
    current = head
    while current.next:
        if count == index:
            break
        left_list = add_item(left_list, current.val)
        count += 1
        current = current.next

    return left_list


def get_half_list_right(head, index):
    right_list = None

    count = 0
    current = head
    while current.next:
        if count >= index:
            right_list = add_item(right_list, current.val)
        count += 1
        current = current.next

    right_list = add_item(right_list, current.val)

    return right_list


def merge_sorting_linked(head: ListNode) -> ListNode | None:
    if head and head.next is None:
        return head

    if head is None:
        return head

    mid = get_middle(head)
    right = mid.next
    mid.next = None

    list_size = count_size_list(head)
    left = merge_sorting_linked(head)
    right = merge_sorting_linked(right)

    return merge_linked(left, right)


def merge_linked(left: ListNode, right: ListNode) -> ListNode:
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


def get_middle(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        # print("slow ", slow.val)
        print("fast ", fast.val)

    return slow


node1 = ListNode(1)
node3 = ListNode(9)
node4 = ListNode(3)
node5 = ListNode(6)
node6 = ListNode(4)
node7 = ListNode(5)
node8 = ListNode(7)
node9 = ListNode(9)

node1.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

# print(merge([1], []))

node = merge_sorting_linked(node1)
print()
# merge_sorting([1, 2, 1, 43, 12, 2])
