import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    table_A = list(map(int, input().split()))
    table_B = list(map(int, input().split()))

    for j in range(4, 0, -1):
        a, b = table_A[1:].count(j), table_B[1:].count(j)
        if a > b:
            print('A')
            break
        elif a < b:
            print('B')
            break
    else:
        print('D')