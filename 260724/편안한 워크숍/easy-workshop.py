import sys
input = sys.stdin.readline

n, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
def dfs(x, y, diff):
    if dp[x][y] != -1:
        return dp[x][y]

    count = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n and 0 < table[nx][ny] - table[x][y] <= diff:
            count = max(count, 1 + dfs(nx, ny, diff))
        
    dp[x][y] = count
    return dp[x][y]

answer = -1
start, end = 0, 10**8
while start <= end:
    l = (start + end) // 2
    dp = [[-1] * n for _ in range(n)]
    is_true = False
    for i in range(n):
        for j in range(n):
            if dfs(i, j, l) >= k:
                is_true = True
    if is_true:
        answer = l
        end = l - 1

    else:
        start = l + 1
print(answer)