import sys
input = sys.stdin.readline

def binary(start, end, num):
    mid = (start + end) // 2
    if table[mid] == num:
        return 1
    if end == start:
        return 0

    if num > table[mid]:
        return binary(mid + 1, end, num)
    else:
        return binary(start, mid, num)


N = int(input().strip())
table = list(map(int, input().split()))
M = int(input().strip())
order = list(map(int, input().split()))
table.sort()
for i in order:
    result = binary(0, N - 1, i)
    print(result)