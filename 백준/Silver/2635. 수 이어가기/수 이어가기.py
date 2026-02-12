import sys
input = sys.stdin.readline

def calculate(num1, num2):
    global max_cnt, max_list
    cnt = 2
    check = [num1, num2]
    while num1 - num2 >= 0:
        num1, num2 = num2, num1 - num2
        cnt += 1
        check.append(num2)
    if cnt > max_cnt:
        max_cnt = cnt
        max_list = check

N = int(input().strip())
max_cnt = 2
max_list = []

for i in range(1, N + 1):
    calculate(N, i)
print(max_cnt)
print(*max_list)