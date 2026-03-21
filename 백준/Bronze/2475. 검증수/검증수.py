import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
result = 0
for i in nums:
    result += i ** 2

print(result % 10)