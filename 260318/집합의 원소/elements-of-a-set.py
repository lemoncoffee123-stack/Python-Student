def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y
    return

def find(x):
    if uf[x] == x:
        return x
    root_node = find(uf[x])
    uf[x] = root_node
    return root_node



N, M = map(int, input().split())
uf = [i for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print(1)
        else:
            print(0)