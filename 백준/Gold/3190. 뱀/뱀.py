import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())
table = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    x, y = map(int, input().split())
    table[x][y] = 2
L = int(input().strip())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
mapping = {'L': 3, 'D': 1}
dir_num = 0
cnt = 0
queue = deque([(1, 1)])
table[1][1] = 1

order = []
order_idx = []
idx = 0

for _ in range(L):
    X, C = input().split()
    order.append(int(X) - cnt)
    order_idx.append(mapping[C])


while True:
    x, y = queue[0]
    is_apple = False

    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if 1 <= nx <= N and 1 <= ny <= N:
        if table[nx][ny] == 2:
            is_apple = True

        elif table[nx][ny] == 1:
            print(cnt + 1)
            exit()

        queue.appendleft((nx, ny))
        if not is_apple:
            x1, y1 = queue.pop()
            table[x1][y1] = 0
        table[nx][ny] = 1
        is_move = True
        cnt += 1

    else:
        print(cnt + 1)
        exit()

    if idx < L and order[idx] == cnt:
        dir_num = (dir_num + order_idx[idx]) % 4
        idx += 1