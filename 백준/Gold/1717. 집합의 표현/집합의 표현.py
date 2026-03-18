import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


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
for _ in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")