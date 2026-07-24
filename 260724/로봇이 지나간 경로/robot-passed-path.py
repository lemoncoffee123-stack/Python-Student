from collections import deque
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
table = [list(input().strip()) for _ in range(h)]


dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

# 찾은 #의 4칸을 확인하여 스타트 지점 찾기
start_point = []

for i in range(h):
    for j in range(w):
        if table[i][j] == '#':
            cnt = 0
            dir = -1
            for k in range(4):
                nx, ny = i + dxs[k], j + dys[k]

                if 0 <= nx < h and 0 <= ny < w and table[nx][ny] == '#':
                    cnt += 1
                    dir = k

            if cnt == 1:
                start_point.append((i, j, dir))


# 찾은 스타트 지점 중 행이 가장 큰 좌표 및 방향 정하기
start_point.sort(lambda x: (-x[0], -x[1]))
x, y, dir = start_point[0]

print(x + 1, y + 1)

dir_to_str = {
    0: '^',
    1: '>',
    2: 'v',
    3: '<'
}

print(dir_to_str[dir])


# 찾은 스타트 지점을 bfs를 진행하여 명령어를 조사
order_list = []
def bfs(a, b, dir):
    queue = deque()
    queue.append((a, b))

    visited = [[False] * w for _ in range(h)]
    visited[a][b] = True
    dir = dir

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dxs[i], y + dys[i]

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and table[nx][ny] == '#':
                if (i + 1) % 4 == dir: 
                    order_list.append('L')
                    dir = i
                elif (i + 3) % 4 == dir:
                    order_list.append('R')
                    dir = i

                order_list.append('A')

                visited[nx][ny] = True
                nx, ny = nx + dxs[i], ny + dys[i]
                visited[nx][ny] = True
                queue.append((nx, ny))

bfs(x, y, dir)
print(''.join(order_list))