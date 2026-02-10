import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
table = [list(input().strip()) for _ in range(N)]

presum_B = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        now_check = (i + j) % 2 == 0

        difference_B = 0
        if now_check:
            if table[i-1][j-1] != 'B':
                difference_B = 1
        else:
            if table[i-1][j-1] != 'W':
                difference_B = 1

        presum_B[i][j] = presum_B[i-1][j] + presum_B[i][j-1] - presum_B[i-1][j-1] + difference_B

min_cnt = float('inf')

for i in range(K, N + 1):
    for j in range(K, M + 1):
        cnt_B = presum_B[i][j] - presum_B[i-K][j] - presum_B[i][j-K] + presum_B[i-K][j-K]

        cnt_W = (K * K) - cnt_B

        min_cnt = min(min_cnt, cnt_W, cnt_B)

print(min_cnt)