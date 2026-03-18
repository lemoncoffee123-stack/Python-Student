import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def union(x, y):
    X, Y = find(x), find(y)
    if X != Y:
        uf[X] = Y


def find(x):
    if uf[x] == x:
        return x

    uf[x] = find(uf[x])
    return uf[x]


n, m = map(int, input().split())
uf = [i for i in range(n)]
for i in range(1, m+1):
    a, b = map(int, input().split())

    if find(a) == find(b):
        print(i)
        exit()

    union(a, b)
else:
    print(0)