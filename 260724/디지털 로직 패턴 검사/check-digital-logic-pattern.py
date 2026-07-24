import sys
input = sys.stdin.readline

S = input().strip()
k, m = map(int, input().split())

dp = {}

for i in range(len(S) - k):
    num = int(S[i:i+k], 2)
    if num not in dp:
        dp[num] = 1
    else:
        dp[num] += 1

for value in dp.values():
    if value >= m:
        print(1)
        exit()
print(0)
