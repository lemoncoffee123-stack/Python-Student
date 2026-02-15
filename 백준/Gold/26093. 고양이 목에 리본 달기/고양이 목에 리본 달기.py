import sys
input = sys.stdin.readline

N, K = map(int, input().split())

last_max_cnt1 = (0, -1)
last_max_cnt2 = (0, -2)

for i in range(N):
    table = list(map(int, input().split()))

    max_cnt1 = (-1, -1)
    max_cnt2 = (-1, -1)

    for j in range(K):
        if j != last_max_cnt1[1]:
            total_cnt = last_max_cnt1[0] + table[j]
        else:
            total_cnt = last_max_cnt2[0] + table[j]

        if total_cnt > max_cnt1[0]:
            max_cnt2 = max_cnt1
            max_cnt1 = (total_cnt, j)
        elif total_cnt > max_cnt2[0]:
            max_cnt2 = (total_cnt, j)

    last_max_cnt1 = max_cnt1
    last_max_cnt2 = max_cnt2

print(last_max_cnt1[0])