import sys
input = sys.stdin.readline

T = int(input().strip())
for tc in range(T):
    N = int(input().strip())
    cost = [tuple(map(int, input().split())) for _ in range(N)]
    weight_per_cost = []
    for weight, val in cost:
        wpc = val / weight
        weight_per_cost.append((wpc, val))

    weight_per_cost.sort()
    print(weight_per_cost[0][1])