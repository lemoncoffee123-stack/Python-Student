# 슬라이딩 윈도우와 파라메트릭 서치를 통한 탐색
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
hole_idx = list(map(int, input().split()))


# 슬라이딩 윈도우 함수 구현
def patch(l):
    cnt = 0
    length = 0
    for i in hole_idx:
        if length <= i:
            length = i + l
            cnt += 1
    return cnt

# 파라메트릭 서치 구현
start, end = 1, 10 ** 9
answer = 0

while start <= end:
    mid = (start + end) // 2

    count = patch(mid)

    if count > k:
        start = mid + 1
    
    else:
        answer = mid
        end = mid - 1

print(answer)