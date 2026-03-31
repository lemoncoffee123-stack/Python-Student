import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dist = [float('inf')] * (N + 1)
dist[1] = 0
adj = []
is_minus = False

for _ in range(M):
    a, b, val = map(int, input().split())
    adj.append((a, b, val))

for i in range(N):
    for u, v, cost in adj:
        if dist[u] != float('inf') and dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost

            if i == N - 1:
                is_minus = True

if is_minus:
    print(-1)
    exit()
else:
    for i in range(2, N + 1):
        if dist[i] != float('inf'):
            print(dist[i])
        else:
            print(-1)