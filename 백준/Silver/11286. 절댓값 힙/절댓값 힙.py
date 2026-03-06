import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
queue = []
for _ in range(N):
    a = int(input().strip())
    if a == 0:
        if queue:
            x, y = heapq.heappop(queue)
            print(y)
        else:
            print(0)
    elif a < 0:
        heapq.heappush(queue, (abs(a), a))
    else:
        heapq.heappush(queue, (a, a))
