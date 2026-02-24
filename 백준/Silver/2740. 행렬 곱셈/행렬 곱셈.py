import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table_A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
table_B = [list(map(int, input().split())) for _ in range(M)]

result = [[] for _ in range(N)]
for i in range(N):
    for j in range(K):
        cnt = 0
        for k in range(M):
            cnt += table_A[i][k] * table_B[k][j]
        result[i].append(cnt)
for i in result:
    print(*i)