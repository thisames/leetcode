from collections import deque

t, l, o, d = map(int, input().split())

hashmap = {}

for i in range(l):
    line = list(map(int, input().split()))
    for j in line[1:]:
        if j not in hashmap:
            hashmap[j] = set(line[1:])
        else:
            hashmap[j].update(line[1:])

fila = deque()
fila.append((o, 0))
visitados = set()
visitados.add(o)

while fila:
    atual, trocas = fila.popleft()

    if atual == d:
        print(trocas)
        break

    for prox in hashmap.get(atual, []):
        if prox not in visitados:
            visitados.add(prox)
            fila.append((prox, trocas + 1))

'''
10 9 1 10
2 1 2
2 2 3
2 3 4
2 4 5
3 5 6 7
2 6 7
2 7 8
2 8 9
2 9 10


10 5 2 10
5 4 3 8 2 1
3 5 10 7
2 1 5
3 6 8 10
3 9 4 5
'''
