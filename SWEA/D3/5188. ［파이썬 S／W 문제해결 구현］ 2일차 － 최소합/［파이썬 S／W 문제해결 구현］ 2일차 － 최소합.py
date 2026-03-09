T = int(input())


def backtracking(x, y, num):
    global min_cnt
    if x >= N or y >= N:
        return

    elif x == N - 1 and y == N - 1:
        if num + table[x][y] < min_cnt:
            min_cnt = num + table[x][y]
        return

    else:
        backtracking(x + 1, y, num + table[x][y])
        backtracking(x, y + 1, num + table[x][y])


for tc in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    min_cnt = 1000
    backtracking(0, 0, 0)
    print(f"#{tc} {min_cnt}")