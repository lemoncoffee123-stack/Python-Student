import sys
input = sys.stdin.readline

def update(idx, val):
    bucket[idx//size] += val - data[idx]
    data[idx] = val

def query(left, right):
    cnt = 0
    while left <= right and left % size != 0:
        cnt += data[left]
        left += 1

    while left + size <= right:
        cnt += bucket[left // size]
        left += size

    while left <= right:
        cnt += data[left]
        left += 1

    return cnt


N, M, K = map(int, input().split())
size = int(N ** 0.5)
data = [int(input()) for _ in range(N)]

bucket = [0] * (N // size + 1)
for i in range(N):
    bucket[i // size] += data[i]

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b - 1, c)
    elif a == 2:
        print(query(b - 1, c - 1))