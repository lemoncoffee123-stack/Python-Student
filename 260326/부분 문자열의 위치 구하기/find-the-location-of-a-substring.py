N = input()
L = input()
n = len(N)
l = len(L)

p = 31
mod = 10**9 + 7

p_mod = [0] * (n  + 1)
p_mod[0] = 1

def to_int(num):
    return ord(num) - ord('a') + 1


for i in range(1, n + 1):
    p_mod[i] = (p_mod[i - 1] * p) % mod

l_h, n_h = 0, 0
for i in range(l):
    l_h = (l_h * p + to_int(L[i])) % mod
    n_h = (n_h * p + to_int(N[i])) % mod

if l_h == n_h:
    print(0)
    exit()

p_l = p_mod[l]
for i in range(1, n - l + 1):
    n_h = (n_h * p - to_int(N[i - 1]) * p_l + to_int(N[i + l - 1])) % mod

    if n_h == l_h:
        print(i)
        exit()

print(-1)