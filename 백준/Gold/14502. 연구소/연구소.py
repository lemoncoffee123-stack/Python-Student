import sys
from collections import deque
input = sys.stdin.readline

def backtracking(x, y, num):
    global max_cnt
    if num == 3:
        max_cnt = max(max_cnt, bfs(start_point))
        return

    for i in range(x, N):
        if i != x:
            y = 0

        for j in range(y, M):
            if not table[i][j]:
                table[i][j] = 1

                backtracking(i, j + 1, num + 1)

                table[i][j] = 0

    return


def bfs(idx):
    queue = deque(idx)
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    check = [[0] * M for _ in range(N)]
    temp = [[] for _ in range(N)]
    for i in range(N):
        temp[i] = table[i][:]

    while queue:
        x, y = queue.popleft()

        for dx ,dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not temp[nx][ny] and not check[nx][ny]:
                check[nx][ny] = 1
                temp[nx][ny] = 2
                queue.append((nx, ny))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not temp[i][j]:
                cnt += 1

    return cnt

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

start_point = []
max_cnt = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 2:
            start_point.append((i, j))

backtracking(0, 0, 0)
print(max_cnt)