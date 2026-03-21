import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = N
while N > 0:
    result += N // M
    N = N // M
print(result)