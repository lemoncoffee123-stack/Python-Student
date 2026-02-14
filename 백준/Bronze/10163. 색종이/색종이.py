import sys
input = sys.stdin.readline

N = int(input().strip())
grid = [[0] * 1001 for _ in range(1001)]
cnt_list = [0] * (N + 1)
for k in range(1, N + 1):
    x, y, width, length = map(int, input().split())
    for i in range(x, x + width):
        grid[i][y:y + length] = [k] * length

for i in range(1001):
    for j in range(1001):
        if grid[i][j] != 0:
            cnt_list[grid[i][j]] += 1

for i in range(1, N + 1):
    print(cnt_list[i])