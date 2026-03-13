import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
queue_low = []
queue_high = []
for i in range(N):
    n = int(input().strip())

    heapq.heappush(queue_low, -n)

    max_val = - heapq.heappop(queue_low)
    heapq.heappush(queue_high, max_val)

    if len(queue_high) > len(queue_low):
        min_val = heapq.heappop(queue_high)
        heapq.heappush(queue_low, - min_val)

    print(- queue_low[0])