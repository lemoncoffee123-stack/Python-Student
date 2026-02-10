import sys
from collections import deque
input = sys.stdin.readline

def bfs(num1, num2, state):
    queue = deque([(num1, num2, state)])
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    while queue:
        x, y, z = queue.popleft()

        if x == N - 1 and y == M - 1:
            return check[x][y][z]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not check[nx][ny][z]:
                if table[nx][ny] == '0':
                    check[nx][ny][z] = check[x][y][z] + 1
                    queue.append((nx, ny, z))

                elif table[nx][ny] == '1' and z == 0:
                    check[nx][ny][z+1] = check[x][y][z] + 1
                    queue.append((nx, ny, z + 1))
    return -1

N, M = map(int, input().split())
table = [list(input().strip()) for _ in range(N)]

check = [[[0] * 2 for _ in range(M)] for _ in range(N)]
check[0][0][0] = 1
print(bfs(0, 0, 0))
