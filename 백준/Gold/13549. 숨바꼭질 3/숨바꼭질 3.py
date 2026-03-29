import heapq, sys
input = sys.stdin.readline


def dijkstra(x, K):
    queue = [(0, x)]
    visited = [float('inf')] * 100001
    visited[x] = 0

    while queue:
        time, x = heapq.heappop(queue)
        
        if visited[x] < time:
            continue
            
        if x == K:
            print(time)
            return

        if 2 * x < 100001 and visited[2 * x] > time:
            visited[2 * x] = time
            heapq.heappush(queue, (time, 2 * x))

        for nx in (x - 1, x + 1):
            if 0 <= nx < 100001 and visited[nx] > time + 1:
                visited[nx] = time  +1
                heapq.heappush(queue, (time + 1, nx))

N, K = map(int, input().split())
dijkstra(N, K)