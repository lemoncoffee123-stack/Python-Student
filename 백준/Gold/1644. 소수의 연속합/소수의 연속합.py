import sys
input = sys.stdin.readline

N = int(input().strip())
if N == 1:
    print(0)
    exit()

prime_check = [True] * (N + 1)
prime_check[0] = prime_check[1] = False
for i in range(2, int(N ** 0.5) + 1):
    if prime_check[i]:
        for j in range(i * i, N + 1, i):
            prime_check[j] = False

prime = [i for i, is_prime in enumerate(prime_check) if is_prime]

i, j = 0, 0
count = prime[i]
result = 0
while i <= j <= len(prime):
    if count == N:
        result += 1
        count -= prime[i]
        i += 1

    elif count > N:
        count -= prime[i]
        i += 1

    elif count < N:
        j += 1
        if j < len(prime):
            count += prime[j]

print(result)