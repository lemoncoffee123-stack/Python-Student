import sys
input = sys.stdin.readline

N = int(input().strip())
table = [0] + list(map(int, input().split()))
S = int(input().strip())
student = [list(map(int, input().split())) for _ in range(S)]

for i in range(S):
    male, number = student[i][0], student[i][1]
    if male == 1:
        for j in range(number, N + 1, number):
            table[j] = (table[j] + 1) % 2
    else:
        table[number] = (table[number] + 1) % 2
        for j in range(0, N):
            if number + j <= N and number - j > 0:
                if table[number - j] == table[number + j]:
                    table[number - j] = (table[number - j] + 1) % 2
                    table[number + j] = (table[number + j] + 1) % 2
                else:
                    break
for i in range(1, N + 1):
    print(table[i], end=" ")
    if i % 20 == 0:
        print()
