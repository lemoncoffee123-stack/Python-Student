import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

queue = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

result = []
while queue:
    x = heapq.heappop(queue)
    result.append(x)

    for k in adj[x]:
        indegree[k] -= 1
        if indegree[k] == 0:
            heapq.heappush(queue, k)

print(*result)