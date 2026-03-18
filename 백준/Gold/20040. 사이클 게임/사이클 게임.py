import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
uf = [i for i in range(n)]
for i in range(1, m+1):
    a, b = map(int, input().split())

    curr_a, curr_b = a, b

    while uf[curr_a] != curr_a:
        uf[curr_a] = uf[uf[curr_a]]
        curr_a = uf[curr_a]
    root_a = curr_a

    while uf[curr_b] != curr_b:
        uf[curr_b] = uf[uf[curr_b]]
        curr_b = uf[curr_b]
    root_b = curr_b

    if root_a == root_b:
        print(i)
        exit()

    uf[root_a] = root_b

else:
    print(0)