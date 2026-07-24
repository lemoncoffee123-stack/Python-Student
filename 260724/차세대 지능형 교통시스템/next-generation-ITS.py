import sys, heapq
input = sys.stdin.readline

n, t = map(int, input().split())
light = [[list(map(int, input().split())) for _ in range(n)] for _ in range(n)]
dir = 1
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
traffic = [
    [],
    [[0, 1, 3], [], [], []],
    [[], [2, 1, 0], [], []],
    [[], [], [1, 2, 3], []],
    [[], [], [], [0, 2, 3]],
    [[0, 1], [], [], []],
    [[], [1, 2], [], []],
    [[], [], [2, 3], []],
    [[], [], [], [0, 3]],
    [[0, 3], [], [], []],
    [[], [0, 1], [], []],
    [[], [], [1, 2], []],
    [[], [], [], [2, 3]]
]

queue = []
heapq.heappush(queue, (0, 0, 0, dir))
count = 1
visited = [[False] * n for _ in range(n)]
visited[0][0] = True

while queue:
    time, x, y, direction = heapq.heappop(queue)

    if time == t + 1:
        break
    
    now_time = time % 4

    if not visited[x][y]:
                visited[x][y] = True
                count += 1

    traffic_num = light[x][y][now_time]
    for dir_num in traffic[traffic_num][direction]:
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        if 0 <= nx < n and 0 <= ny < n:
            heapq.heappush(queue, (time + 1, nx, ny, dir_num))

print(count)