class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.indios = []


n, e = map(int, input().split())
positions = {}

for i in range(e):
    v, d = map(int, input().split())
    positions[v] = d

tora = {}
head = ListNode(1)
curr = head

for i in range(2, n + 1):
    new_node = ListNode(i)
    if i in positions:
        new_node.indios.append(positions[i])
    curr.next = new_node
    new_node.prev = curr
    curr = curr.next
curr.next = head
head.prev = curr


def get_state(head):
    state = set()
    curr = head
    for _ in range(n):
        if curr.indios:
            state.add(curr.val)
        curr = curr.next
    return state


initial_state = get_state(head)

steps = 0
while True:
    steps += 1
    curr = head
    movement = []
    for _ in range(n):
        for direction in curr.indios:
            if direction == 1:
                movement.append((curr, curr.next, direction))
            else:
                movement.append((curr, curr.prev, direction))
        curr = curr.next

    curr = head
    for _ in range(n):
        curr.indios = []
        curr = curr.next

    destino_map = {}
    for origem, destino, direcao in movement:
        key = destino.val
        if key not in destino_map:
            destino_map[key] = []
        destino_map[key].append((origem, direcao))

    for key, entradas in destino_map.items():
        if len(entradas) == 1:
            _, direcao = entradas[0]
            destino = head
            for _ in range(key - 1):
                destino = destino.next
            destino.indios.append(direcao)
        elif len(entradas) == 2:
            print()
            destino = head
            for _ in range(key - 1):
                destino = destino.next
            destino.indios.append(-entradas[0][1])
            destino.indios.append(-entradas[1][1])
    if get_state(head) == initial_state:
        break

print(steps)
'''
6 4
2 1
3 1
5 1
6 1

8 6
2 -1
3 1
4 -1
6 1
7 -1
8 1
'''
