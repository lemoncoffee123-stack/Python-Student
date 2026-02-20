import sys
input = sys.stdin.readline

N = int(input().strip())
table = [list(tuple(map(int, input().split()))) for _ in range(N)]
table.sort(key=lambda x: (x[1], x[0]))
s, e = table[0][0], table[0][1]
cnt = 1
for i in range(1, N):
    if e <= table[i][0]:
        cnt += 1
        s, e = table[i][0], table[i][1]
print(cnt)