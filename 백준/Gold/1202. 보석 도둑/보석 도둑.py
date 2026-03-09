import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewel = []
for _ in range(N):
    a, b = map(int, input().split())
    jewel.append((a, b))

bag = []
for _ in range(K):
    bag.append(int(input()))
    
jewel.sort()
bag.sort()

queue = []
result = 0
idx = 0
for i in bag:
    while idx < N and jewel[idx][0] <= i:
        heapq.heappush(queue, -jewel[idx][1])
        idx += 1

    if queue:
        result += - heapq.heappop(queue)

print(result)