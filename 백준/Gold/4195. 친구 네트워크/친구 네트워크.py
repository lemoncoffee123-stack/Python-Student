import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def union(x, y):
    X, Y = find(x), find(y)
    if X != Y:
        names[X] = Y
        size[Y] += size[X]
    print(size[Y])


def find(x):
    if x not in names:
        names[x] = x
        size[x] = 1
        return x

    if names[x] == x:
        return x

    names[x] = find(names[x])
    return names[x]


T = int(input().strip())
for _ in range(T):
    names = {}
    size = {}
    f = int(input().strip())
    for _ in range(f):
        a, b = input().split()
        union(a, b)

