import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
i = 0
result = N + 1

count = 0
for j in range(N):
    count += nums[j]

    while count >= S:
        result = min(result, j - i + 1)
        count -= nums[i]
        i += 1

if result == N + 1:
    print(0)
else:
    print(result)