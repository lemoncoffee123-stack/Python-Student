import sys
from collections import defaultdict
input = sys.stdin.readline

n, L = input().split()
n = int(n)
l = len(L)

p1, p2 = 31, 37
mod1, mod2 = 10**9 + 7, 10**9 + 9

p1_l, p2_l = pow(p1, n, mod1), pow(p2, n, mod2)

L_arr = [ord(c) - 96 for c in L]

h1, h2 = 0, 0
for i in range(n):
    h1 = (h1 * p1 + L_arr[i]) % mod1
    h2 = (h2 * p2 + L_arr[i]) % mod2

counts = defaultdict(int)
counts[(h1, h2)] = 1

for i in range(1, l - n + 1):
    h1 = (h1 * p1 - L_arr[i - 1] * p1_l + L_arr[i + n - 1]) % mod1
    h2 = (h2 * p2 - L_arr[i - 1] * p2_l + L_arr[i + n - 1]) % mod2

    if h1 < 0:
        h1 += mod1
    if h2 < 0:
        h2 += mod2

    counts[(h1, h2)] += 1

print(max(counts.values()))