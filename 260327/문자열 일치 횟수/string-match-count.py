N = int(input())
T, P = input(), input()
n, m = len(T), len(P)
T = "#" + T
P = "#" + P * ((N - 1) // m + 2)
m = m + N - 1

f = [0] * (n + 1)
f[0] = - 1
for i in range(1, n + 1):
    j = f[i - 1]
    while j >= 0 and T[j + 1] != T[i]:
        j = f[j]
    
    f[i] = j + 1

j = 0
result = 0
for i in range(1, m + 1):
    while j >= 0 and T[j + 1] != P[i]:
        j = f[j]
    
    j += 1

    if j == n:
        result += 1
        j = f[j]

print(result)