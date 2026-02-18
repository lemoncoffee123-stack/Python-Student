import sys
input = sys.stdin.readline

def backtracking(num, num1):
    global min_chicken
    if num == M:
        cnt = 0
        for i in range(N):
            for j in range(N):
                if table[i][j] == 1:
                    cnt_list = []
                    for k in range(M):
                        x, y = use_chicken[k]
                        cnt_list.append((abs(i - x) + abs(j - y)))
                    cnt += min(cnt_list)
        min_chicken = min(min_chicken, cnt)
        return

    for i in range(num1, len(chicken_idx)):
        use_chicken.append(chicken_idx[i])

        backtracking(num + 1, i + 1)

        use_chicken.pop()


N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
chicken_idx = []
for i in range(N):
    for j in range(N):
        if table[i][j] == 2:
            chicken_idx.append((i, j))
use_chicken = []
min_chicken = N ** 4

backtracking(0, 0)
print(min_chicken)