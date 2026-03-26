import sys
input = sys.stdin.readline

N = input().strip()
L = input().strip()
n = len(N)
l = len(L)

p = 31
mod = 10**9 + 7

p_mod = [0] * (n  + 1)
p_mod[0] = 1

N_arr = [ord(c) - 96 for c in N]
L_arr = [ord(c) - 96 for c in L]

for i in range(1, n + 1):
    p_mod[i] = (p_mod[i - 1] * p) % mod

l_h, n_h = 0, 0
for i in range(l):
    l_h = (l_h * p + L_arr[i]) % mod
    n_h = (n_h * p + N_arr[i]) % mod

if l_h == n_h:
    print(0)
    exit()

p_l = p_mod[l]
for i in range(1, n - l + 1):
    n_h = (n_h * p - N_arr[i - 1] * p_l + N_arr[i + l - 1]) % mod

    if n_h == l_h:
        print(i)
        exit()

print(-1)