def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


def find(x):
    if uf[x] == x:
        return x

    uf[x] = find(uf[x])
    return uf[x]


n, m = map(int, input().split())
uf = [i for i in range(n + 1)]
is_connected = False
for i in range(m):
    a, b = map(int, input().split())

    if find(a) == find(b):
        is_connected = True
        idx = i + 1
        break

    union(a, b)

if is_connected:
    print(idx)

else:
    print("happy")