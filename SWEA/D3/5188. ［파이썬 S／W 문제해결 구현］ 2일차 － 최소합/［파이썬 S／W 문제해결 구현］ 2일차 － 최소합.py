def solve(r, c, cost):
    global min_cost
    if r >= N or c >= N:  # 비정상 범위
        return
    if (r, c) == (N - 1, N - 1):  # 우측하단, 목적지 도착
        # 비용계산
        total = cost + data[r][c]
        if total < min_cost:
            min_cost = total
        return
    # 현재 위치 r,c에서 내가 할 수 있는 일?
    # 오른쪽 이동, 아래쪽 이동
    solve(r, c + 1, cost + data[r][c])
    solve(r + 1, c, cost + data[r][c])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 1000
    solve(0, 0, 0)
    print(f'#{tc} {min_cost}')