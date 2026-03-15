import sys, heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(x):
    dist = [INF] * (V + 1)
    queue = []
    heapq.heappush(queue, (0, x))
    dist[x] = 0

    while queue:
        cnt, x = heapq.heappop(queue)

        if dist[x] < cnt:
            return

        for nx, val in adj[x]:
            if dist[nx] > cnt + val:
                dist[nx] = cnt + val
                heapq.heappush(queue, (cnt + val, nx))

    find_num = max(dist[1:])
    for idx, i in enumerate(dist):
        if i == find_num:
            return idx, i


V = int(input().strip())
adj = [[] for _ in range(V + 1)]
for _ in range(V):
    data = list(map(int, input().split()))
    a = data[0]
    for i in range(1, len(data), 2):
        if data[i] == -1:
            break

        b, val = data[i], data[i + 1]
        adj[a].append((b, val))

idx, max_cnt = dijkstra(1)
if idx == 1:
    print(max_cnt)
else:
    idx2, result = dijkstra(idx)
    print(result)