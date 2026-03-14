import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    queue = deque([x])
    visited[x] = 0

    while queue:
        x = queue.popleft()

        for nx in adj[x]:
            if visited[nx] == INF:
                visited[nx] = x
                queue.append(nx)

INF = float('inf')
N = int(input().strip())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [INF] * (N + 1)
bfs(1)
for i in range(2, N + 1):
    print(visited[i])