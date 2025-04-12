import heapq

n, m, c = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    xi, yi, ti = map(int, input().split())
    adj[xi].append((yi, ti))
    adj[yi].append((xi, ti))

posicoes = list(map(int, input().split()))


def dijkstra(n, adj, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist


dist = dijkstra(n, adj, 1)

min_graph = [[] for _ in range(n + 1)]
for u in range(1, n + 1):
    for v, w in adj[u]:
        if dist[u] == dist[v] + w:
            min_graph[u].append(v)

count = 0
for i in min_graph:
    if len(i) > 0:
        count += 1
print(count)
