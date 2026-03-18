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

n, m = map(int, input().split())
uf = [i for i in range(n + 1)]
for _ in range(m):
    data = list(input().split())
    if data[0] == 'x':
        union(int(data[1]), int(data[2]))
    else:
        cnt = 0
        for i in range(1, n + 1):
            if find(int(data[1])) == find(i):
                cnt += 1

        print(cnt)