class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


while True:
    n = int(input())
    if n == 0:
        break

    head = Node(1)
    current = head
    for i in range(2, n + 1):
        current.next = Node(i)
        current = current.next
    current.next = head

    trywith = 0
    results = dict()
    current = head
    while len(results) != n or list(results)[-1] != 13:
        trywith += 1
        results = dict()
        current = head
        count = 1
        while len(results) != n:
            if current.val not in results:
                results[current.val] = count
            j = 0
            while j != trywith and len(results) != n:
                current = current.next
                if current.val not in results:
                    j += 1
            count += 1
        # print(trywith, list(results))

    print(trywith)
