N = int(input())
M = int(input())
uf = list(range(N + 1))
for _ in range(M):
    a = int(input())
    root_a = a
    while root_a != uf[root_a]:
        uf[root_a] = uf[uf[root_a]]
        root_a = uf[root_a]
    if root_a == 0:
        break
    uf[root_a] -= 1


result = 0
for i in range(1, N + 1):
    if uf[i] != i:
        result += 1
print(result)