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


n = int(input().strip())
m = int(input().strip())
uf = [i for i in range(n + 1)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union(i + 1, j + 1)

city = list(map(int, input().split()))
for i in city:
    if find(city[0]) != find(i):
        print("NO")
        exit()

else:
    print("YES")