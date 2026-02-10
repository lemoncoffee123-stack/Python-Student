T = int(input())
from collections import deque

def bfs(num1, num2):
    check1 = [[0] * N for _ in range(N)]
    queue = deque([(num1, num2)])
    check1[num1][num2] = 1
    check2[num1][num2] = 1
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    max_cnt = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not check1[nx][ny] and table[nx][ny] == table[x][y] + 1:
                check1[nx][ny] = check1[x][y] + 1
                check2[nx][ny] = 1
                queue.append((nx, ny))

    for i in range(N):
        for j in range(N):
            if check1[i][j] > max_cnt:
                max_cnt = check1[i][j]

    return max_cnt

for tc in range(1, 1 + T):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    check2 = [[0] * N for _ in range(N)]
    num_list = [0] * (N**2 + 1)

    for i in range(N):
        for j in range(N):
            if not check2[i][j]:
                num_list[table[i][j]] = bfs(i, j)

    cnt = max(num_list)
    idx = num_list.index(cnt)

    print(f"#{tc} {idx} {cnt}")