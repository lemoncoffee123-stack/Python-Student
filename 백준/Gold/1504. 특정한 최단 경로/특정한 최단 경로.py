import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, end):
    dist = [INF] * (N + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0

    while queue:
        distance, x = heapq.heappop(queue)

        if distance > dist[x]:
            continue

        if x == end:
            continue

        for nx, val in adj[x]:
            count = dist[x] + val
            if dist[nx] > count:
                dist[nx] = count
                heapq.heappush(queue, (count, nx))

    return dist[end]

N, E = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

v1, v2 = map(int, input().split())
cnt1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
cnt2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
result = min(cnt1, cnt2)
if result != INF:
    print(result)
else:
    print(-1)