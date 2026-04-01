import sys, heapq
input = sys.stdin.readline


def dijkstra(start):
    queue = []
    for nx, cost in adj[start]:
        if cost < dist[start][nx]:
            dist[start][nx] = cost
            heapq.heappush(queue, (cost, nx))

    while queue:
        val, x = heapq.heappop(queue)

        if dist[start][x] < val:
            continue

        if x == start:
            return val

        for kx, weight in adj[x]:
            cost_result = val + weight
            if cost_result < dist[start][kx]:
                dist[start][kx] = cost_result
                heapq.heappush(queue, (cost_result, kx))

    return float('inf')

V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
dist = [[float('inf')] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

result = float('inf')
for i in range(1, V + 1):
    result = min(result, dijkstra(i))

if result != float('inf'):
    print(result)
else:
    print(-1)