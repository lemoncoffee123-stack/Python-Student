T = int(input())

def russia(num1, num2):
    cnt = 0

    for i in range(0, num1):
        for j in range(M):
            if table[i][j] != 'W':
                cnt += 1

    for i in range(num1, num2):
        for j in range(M):
            if table[i][j] != 'B':
                cnt += 1

    for i in range(num2, N):
        for j in range(M):
            if table[i][j] != 'R':
                cnt += 1

    return cnt

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    table = [input() for _ in range(N)]

    min_cnt = M * N

    for i in range(1, N - 1):
        for j in range(i + 1, N):
            min_cnt = min(min_cnt, russia(i, j))

    print(f"#{tc} {min_cnt}")