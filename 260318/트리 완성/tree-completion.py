n, m = map(int, input().split())
uf = [i for i in range(n + 1)]
cnt = 0
lines = 0
for _ in range(m):
    a, b = map(int, input().split())

    curr_a, curr_b = a, b

    while uf[curr_a] != curr_a:
        uf[curr_a] = uf[uf[curr_a]]
        curr_a = uf[curr_a]

    while uf[curr_b] != curr_b:
        uf[curr_b] = uf[uf[curr_b]]
        curr_b = uf[curr_b]

    root_a, root_b = curr_a, curr_b

    if root_a == root_b:
        cnt += 1
        continue
    else:
        uf[root_a] = root_b
        lines += 1

cnt += (n - 1) - lines
print(cnt)