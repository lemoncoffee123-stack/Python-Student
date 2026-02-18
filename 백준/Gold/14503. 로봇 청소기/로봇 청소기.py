import sys
input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
table[x][y] = 2
cnt = 1
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

while True:
    for i in range(1, 5):
        dir_num = (d + i * 3) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        if table[nx][ny] == 0:
            x, y = nx, ny
            d = dir_num
            table[x][y] = 2
            cnt += 1
            break

    else:
        dir_num = (d + 2) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        if table[nx][ny] != 1:
            x, y = nx, ny
        else:
            print(cnt)
            exit()