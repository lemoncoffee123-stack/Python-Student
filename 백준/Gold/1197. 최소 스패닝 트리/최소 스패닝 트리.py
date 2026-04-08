import sys, heapq
input = sys.stdin.readline


def prim(num):
    queue = []
    heapq.heappush(queue, (0, num))
    nodes[num] = 0
    result = 0

    while queue:
        cnt, x = heapq.heappop(queue)
        if visited[x]:
            continue

        result += cnt
        visited[x] = True

        for nx, val in adj[x]:
            if val < nodes[nx]:
                nodes[nx] = val
                heapq.heappush(queue, (val, nx))

    return result

V, E = map(int, input().split())
nodes = [float('inf')] * (V + 1)
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, val = map(int, input().split())
    adj[a].append((b, val))
    adj[b].append((a, val))
visited = [False] * (V + 1)
print(prim(1))