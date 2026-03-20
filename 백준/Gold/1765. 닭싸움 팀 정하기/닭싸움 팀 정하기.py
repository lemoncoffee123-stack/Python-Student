import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
uf = list(range(N + 1))
enemy = [[] for _ in range(N + 1)]
for _ in range(M):
    word, a, b = input().split()
    a, b = int(a), int(b)

    if word == 'F':
        curr_a, curr_b = a, b
        while uf[curr_a] != curr_a:
            uf[curr_a] = uf[uf[curr_a]]
            curr_a = uf[curr_a]

        while uf[curr_b] != curr_b:
            uf[curr_b] = uf[uf[curr_b]]
            curr_b = uf[curr_b]

        uf[curr_a] = curr_b

    elif word == 'E':
        enemy[a].append(b)
        enemy[b].append(a)

for i in range(1, N + 1):
    if len(enemy[i]) > 1:
        first_e = enemy[i][0]
        for next_e in enemy[i][1:]:
            root_A, root_B = first_e, next_e
            while root_A != uf[root_A]:
                uf[root_A] = uf[uf[root_A]]
                root_A = uf[root_A]
            while root_B != uf[root_B]:
                uf[root_B] = uf[uf[root_B]]
                root_B = uf[root_B]

            uf[root_A] = root_B

result = 0
for i in range(1, N + 1):
    if i == uf[i]:
        result += 1

print(result)