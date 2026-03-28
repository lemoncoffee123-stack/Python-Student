import bisect, sys
input = sys.stdin.readline

N = int(input().strip())
data = list(map(int, input().split()))
bucket_size = int(N ** 0.5)
num_buckets = (N + bucket_size - 1) // bucket_size
buckets = [[] for _ in range(num_buckets)]

for i in range(N):
    b_idx = i // bucket_size
    buckets[b_idx].append(data[i])

for b in buckets:
    b.sort()

def query(i, j ,k):
    res = 0
    start = i // bucket_size
    end = j // bucket_size

    if start == end:
        for idx in range(i, j + 1):
            if data[idx] > k:
                res += 1

    else:
        for idx in range(i, (start + 1) * bucket_size):
            if data[idx] > k:
                res += 1

        for b in range(start + 1, end):
            count = len(buckets[b]) - bisect.bisect_right(buckets[b], k)
            res += count

        for idx in range(end * bucket_size, j + 1):
            if data[idx] > k:
                res += 1

    return res


def update(i, k):
    b_idx = i // bucket_size
    old_val = data[i]

    data[i] = k

    buckets[b_idx].remove(old_val)
    bisect.insort(buckets[b_idx], k)

M = int(input().strip())
for _ in range(M):
    INPUT = list(map(int, input().split()))
    if INPUT[0] == 1:
        print(query(INPUT[1] - 1, INPUT[2] - 1, INPUT[3]))
    elif INPUT[0] == 2:
        update(INPUT[1] - 1, INPUT[2])