import sys
input = sys.stdin.readline

def Binary(start, end):
    global max_cnt
    
    if start > end:
        return

    mid = (start + end) // 2
    cnt = 0
    for i in table:
        cnt += i // mid
    if cnt >= N:
        max_cnt = mid
        Binary(mid + 1, end)
    else:
        Binary(start, mid - 1)


K, N = map(int, input().split())
table = [int(input().strip()) for _ in range(K)]
max_cnt = 0
Binary(1, max(table))
print(max_cnt)