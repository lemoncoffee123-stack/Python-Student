import sys
import heapq
input = sys.stdin.readline

def bfs(queue):
    heapq.heapify(queue)

    while queue:
        cnt, x = heapq.heappop(queue)

        for cnt2, nx in table[x]:
            if check[nx] > cnt + cnt2:
                check[nx] = cnt + cnt2
                heapq.heappush(queue, (cnt + cnt2, nx))

    return


V, E = map(int, input().split())
K = int(input().strip())
table = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    table[a].append((c, b))
check = [0xffffff] * (V + 1)
check[K] = 1

bfs([(1, K)])

for i in range(1, V + 1):
    if check[i] != 0xffffff:
        print(check[i] - 1)
    else:
        print('INF')