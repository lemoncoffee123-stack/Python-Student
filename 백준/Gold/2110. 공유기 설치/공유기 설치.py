import sys
input = sys.stdin.readline

N, C = map(int, input().split())
table = [int(input().strip()) for _ in range(N)]
table.sort()
start = 1
end = table[-1] - table[0]
max_cnt = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    distance = table[0]
    for i in table:
        if i >= distance + mid:
            distance = i
            cnt += 1

    if cnt >= C:
        max_cnt = mid
        start, end = mid + 1, end

    else:
        start, end = start, mid - 1

print(max_cnt)