import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    check = [[0] * N for _ in range(N)]
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    is_moved = False
    for i in range(N):
        for j in range(N):
            if not check[i][j]:
                check[i][j] = 1
                queue = deque([(i, j)])
                cnt = table[i][j]
                temp = [(i, j)]


                while queue:
                    x, y = queue.popleft()

                    for dx, dy in zip(dxs, dys):
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < N and 0 <= ny < N and not check[nx][ny]:
                            if L <= abs(table[x][y] - table[nx][ny]) <= R:
                                check[nx][ny] = 1
                                cnt += table[nx][ny]
                                temp.append((nx, ny))
                                queue.append((nx, ny))

                if len(temp) > 1:
                    is_moved = True
                    k = cnt // len(temp)
                    for x, y in temp:
                        table[x][y] = k

    return is_moved


N, L, R = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
total_cnt = 0
while True:
    if bfs():
        total_cnt += 1
    else:
        break
print(total_cnt)