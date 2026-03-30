import sys, heapq
input = sys.stdin.readline


def dijkstra(start):
    queue = [(0, start)]
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    while queue:
        val, x = heapq.heappop(queue)
        if val > dist[x]:
            continue

        for nx, cost in adj[x]:
            if dist[nx] > val + cost:
                dist[nx] = val + cost
                heapq.heappush(queue, (val + cost, nx))

    result = []
    for i in goal:
        if dist[i] != float('inf') and dist[i] % 2 == 1:
            result.append(i)
    result.sort()
    print(*result)
    return

T = int(input().strip())
for tc in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, val = map(int, input().split())
        cost = 2 * val
        if (a == g and b == h) or (a == h and b == g):
            cost -= 1

        adj[a].append((b, cost))
        adj[b].append((a, cost))

    goal = [int(input()) for _ in range(t)]

    dijkstra(s)