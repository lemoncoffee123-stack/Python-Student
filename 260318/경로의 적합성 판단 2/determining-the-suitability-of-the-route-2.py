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


n, m, k = map(int, input().split())
uf = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

check = list(map(int, input().split()))
for i in check:
    if find(check[0]) != find(i):
        print(0)
        exit()
else:
    print(1)