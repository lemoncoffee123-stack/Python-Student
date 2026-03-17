import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited[start] = True
    v_count = 0
    e_count = 0

    while queue:
        curr = queue.popleft()
        v_count += 1

        for nx in adj[curr]:
            e_count += 1
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)

    if e_count // 2 == v_count - 1:
        return True

    else:
        return False

tc = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        exit()

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            if bfs(i):
                count += 1

    if count == 0:
        print(f"Case {tc}: No trees.")
    elif count == 1:
        print(f"Case {tc}: There is one tree.")
    else:
        print(f"Case {tc}: A forest of {count} trees.")

    tc += 1