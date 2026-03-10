import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
table = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
queue = deque()

for _ in range(M):
    a, b = map(int, input().split())
    indegree[b] += 1
    table[a].append(b)

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    x = queue.popleft()
    result.append(x)

    for nx in table[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            queue.append(nx)

print(*result)