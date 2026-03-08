import sys, heapq
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    M = int(input().strip())
    table = []
    for _ in range(M//10 + 1):
        table.extend(list(map(int, input().split())))
    print(M//2 + 1)
    queue1 = []
    queue2 = []
    print(table[0], end=" ")
    heapq.heappush(queue1, -table[0])

    for i in range(1, M):
        if i % 20 == 0:
            print()

        if table[i] > -queue1[0]:
            heapq.heappush(queue2, table[i])

        else:
            heapq.heappush(queue1, -table[i])

        if len(queue1) > len(queue2) + 1:
            k = - heapq.heappop(queue1)
            heapq.heappush(queue2, k)

        elif len(queue1) + 1 < len(queue2):
            k = heapq.heappop(queue2)
            heapq.heappush(queue1, -k)

        if i % 2 == 0:
            if len(queue1) > len(queue2):
                print(- queue1[0], end=" ")
            else:
                print(queue2[0], end=" ")

    else:
        print()