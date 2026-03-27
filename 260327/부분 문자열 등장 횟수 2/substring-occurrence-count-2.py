T, q = input().split()
n = len(T)
T = "#" + T
for _ in range(int(q)):
    P = input()
    m = len(P)
    P = "#" + P

    f = [0] * (m + 1)
    f[0] = -1
    for i in range(1, m + 1):
        j = f[i - 1]

        while j >= 0 and P[j + 1] != P[i]:
            j = f[j]

        f[i] = j + 1

    j = 0
    result = 0
    for i in range(1, n + 1):
        while j >= 0 and P[j + 1] != T[i]:
            j = f[j]
        
        j += 1

        if j == m:
            result += 1
            j = f[j]

    print(result)