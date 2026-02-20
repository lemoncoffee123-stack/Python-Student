import sys
input = sys.stdin.readline

N = int(input().strip())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

cnt = distance[0] * price[0]
for i in range(1, N - 1):
    if price[i] > price[i - 1]:
        cnt += price[i - 1] * distance[i]
        price[i] = price[i - 1]
    else:
        cnt += price[i] * distance[i]
print(cnt)