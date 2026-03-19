import sys
input = sys.stdin.readline


def find(x):
    root = x
    while parent[root] != root:
        parent[root] = parent[parent[root]]
        root = parent[root]
    return root

N, Q = map(int, input().split())
parent = list(range(N + 1))
sets = [set() for _ in range(N + 1)]

for i in range(1, N + 1):
    sets[i] = set(map(int, input().split()[1:]))

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        u, v = query[1], query[2]
        root_u, root_v = find(u), find(v)

        if root_u != root_v:
            if len(sets[root_u]) < len(sets[root_v]):
                root_u, root_v = root_v, root_u

                sets[root_u].update(sets[root_v])
                sets[root_v], sets[root_u] = sets[root_u], set()
            else:
                sets[root_u].update(sets[root_v])
                sets[root_v] = set()

    elif query[0] == 2:
        u = query[1]
        root_u = find(u)
        print(len(sets[root_u]))