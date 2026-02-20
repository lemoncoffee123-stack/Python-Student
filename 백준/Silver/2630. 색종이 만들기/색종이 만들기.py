import sys
input = sys.stdin.readline

def cut_square(grid, num):
    global cnt_blue, cnt_white
    if num == 1:
        if grid[0][0] == 0:
            cnt_white += 1
        else:
            cnt_blue += 1
        return

    start_point = [(0,0), (num//2, 0), (0, num//2), (num//2, num//2)]
    for x, y in start_point:
        temp = []
        for i in range(x, x + num//2):
            temp_row = []
            for j in range(y, y + num//2):
                temp_row.append(grid[i][j])
            temp.append(temp_row)

        is_same = True

        for i in range(num//2):
            if not is_same:
                break
            for j in range(num//2):
                if temp[i][j] != temp[0][0]:
                    is_same = False
                    cut_square(temp, num//2)
                    break
        if is_same:
            if temp[0][0] == 0:
                cnt_white += 1
            else:
                cnt_blue += 1


N = int(input().strip())
table = [list(map(int, input().split())) for _ in range(N)]
cnt_blue = 0
cnt_white = 0
is_same_color = True

for i in range(N):
    if not is_same_color:
        break
    for j in range(N):
        if table[i][j] != table[0][0]:
            is_same_color = False
            cut_square(table, N)
            break
else:
    if table[0][0] == 0:
        cnt_white += 1
    else:
        cnt_blue += 1
print(cnt_white)
print(cnt_blue)