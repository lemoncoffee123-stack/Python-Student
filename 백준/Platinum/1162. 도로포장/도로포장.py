import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, 0, start))
    dist[start][0] = 0

    while queue:
        distance, k, x = heapq.heappop(queue)

        if distance > dist[x][k]:
            continue

        if x == N:
            return

        for nx, val in adj[x]:
            if k < K:
                count = dist[x][k]
                if dist[nx][k + 1] > count:
                    dist[nx][k + 1] = count
                    heapq.heappush(queue, (count, k + 1, nx))

            count = dist[x][k] + val
            if dist[nx][k] > count:
                dist[nx][k] = count
                heapq.heappush(queue, (count, k, nx))



N, M, K = map(int, input().split())
adj = [[] for _ in range(N + 1)]
dist = [[INF] * (K + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

dijkstra(1)
print(min(dist[N]))