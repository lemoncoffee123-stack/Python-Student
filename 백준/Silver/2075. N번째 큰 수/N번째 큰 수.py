import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
queue = []
for _ in range(N):
    table = list(map(int, input().split()))
    for i in table:
        if len(queue) < N:
            heapq.heappush(queue, i)
        elif i > queue[0]:
            heapq.heappop(queue)
            heapq.heappush(queue, i)
print(queue[0])