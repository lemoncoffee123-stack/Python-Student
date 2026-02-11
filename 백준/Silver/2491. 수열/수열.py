import sys
input = sys.stdin.readline

N = int(input().strip())
table = list(map(int, input().split()))

max_cnt = 1
min_cnt = 1
final_cnt = 1

for i in range(1, N):
    if table[i] >= table[i - 1]:
        max_cnt += 1
    else:
        max_cnt = 1

    if table[i] <= table[i - 1]:
        min_cnt += 1
    else:
        min_cnt = 1

    final_cnt = max(final_cnt, min_cnt, max_cnt)

print(final_cnt)