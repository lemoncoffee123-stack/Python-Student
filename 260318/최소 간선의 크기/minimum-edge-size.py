def find(x):
    if uf[x] == x:
        return x

    uf[x] = uf[uf[x]]
    return uf[x]


n, m = map(int, input().split())
A, B = map(int, input().split())
uf = [i for i in range(n + 1)]
lines = [list(map(int, input().split())) for _ in range(m)]
lines.sort(key=lambda x: x[2], reverse=True)
min_val = float('inf')
for a, b, val in lines:
    curr_a, curr_b = a, b

    while uf[curr_a] != curr_a:
        uf[curr_a] = uf[uf[curr_a]]
        curr_a = uf[curr_a]

    while uf[curr_b] != curr_b:
        uf[curr_b] = uf[uf[curr_b]]
        curr_b = uf[curr_b]

    root_a, root_b = curr_a, curr_b

    uf[root_a] = root_b
    min_val = min(min_val, val)

    if find(A) == find(B):
        print(min_val)
        exit()