import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    adj = [[False] * (N + 1) for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    table = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            adj[table[i]][table[j]] = True
            indegree[table[j]] += 1

    M = int(input().strip())
    for _ in range(M):
        a, b = map(int, input().split())
        if adj[a][b]:
            adj[a][b], adj[b][a] = False, True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            adj[b][a], adj[a][b] = False, True
            indegree[a] -= 1
            indegree[b] += 1

    queue = deque()
    result = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            result.append(i)

    is_impossible = False
    is_question = False
    while queue:
        if len(queue) > 1:
            is_question = True
            break

        x = queue.popleft()
        for i in range(1, N + 1):
            if adj[x][i]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    queue.append(i)
                    result.append(i)

    if len(result) < N:
        is_impossible = True

    if is_question:
        print("?")
    elif is_impossible:
        print("IMPOSSIBLE")
    else:
        print(*result)