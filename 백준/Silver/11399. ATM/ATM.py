import sys
input = sys.stdin.readline

N = int(input().strip())
table = list(map(int, input().split()))
table.sort()
cnt = 0
temp = 0
for i in range(N):
    temp += table[i]
    cnt += temp
print(cnt)