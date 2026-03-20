N, M, K = map(int, input().split())
uf = list(range(N + 1))
groups = [[] for _ in range(N + 1)]
minimum_nums = [float('inf')] * (N + 1)
cost = [0] + list(map(int, input().split()))
for _ in range(M):
    a, b = map(int, input().split())
    curr_a, curr_b = a, b
    while uf[curr_a] != curr_a:
        uf[curr_a] = uf[uf[curr_a]]
        curr_a = uf[curr_a]

    while uf[curr_b] != curr_b:
        uf[curr_b] = uf[uf[curr_b]]
        curr_b = uf[curr_b]

    uf[curr_a] = curr_b

for i in range(1, N + 1):
    root_A = i
    while root_A != uf[root_A]:
        uf[root_A] = uf[uf[root_A]]
        root_A = uf[root_A]

    groups[root_A].append(i)

for i in range(1, N + 1):
    if groups[i]:
        for j in range(len(groups[i])):
            if cost[groups[i][j]] < minimum_nums[i]:
                minimum_nums[i] = cost[groups[i][j]]

result = 0
cnt = 0
min_val = float('inf')
for i in minimum_nums:
    if i != float('inf'):
        result += i
        cnt += 1
    min_val = min(min_val, i)
if cnt <= 1:
    result = 0
else:
    result += min_val * (cnt - 2)
    
if result > K:
    print("NO")
else:
    print(result)