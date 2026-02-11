import sys
input = sys.stdin.readline

N = int(input().strip())
table = [list(map(int, input().split())) for _ in range(N)]
table.sort(key=lambda x: x[1], reverse=True)
idx = table[0][0]
height = table[0][1]
cnt = height
idx_L, idx_R = idx, idx
for i in range(1, N):
    if table[i][0] > idx_R:
        height_R = table[i][1]
        cnt += height_R * (table[i][0] - idx_R)
        idx_R = table[i][0]
    if table[i][0] < idx_L:
        height_L = table[i][1]
        cnt += height_L * (idx_L - table[i][0])
        idx_L = table[i][0]

print(cnt)