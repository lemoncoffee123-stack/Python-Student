def union(x, y):
    X, Y = find(x), find(y)
    if X != Y:
        if X < Y:
            uf[Y] = X

        else:
            uf[X] = Y


def find(x):
    if uf[x] == x:
        return x

    root_node = find(uf[x])
    uf[x] = root_node
    return root_node


n = int(input())
uf = [i for i in range(n + 1)]
result = set()
while True:
    try:
        a, b = map(int, input().split())
        union(a, b)
    except:
        break
for i in range(1, n + 1):
    result.add(find(i))

print(*sorted(list(result)))