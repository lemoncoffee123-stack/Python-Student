import sys
input = sys.stdin.readline

def counting(num, grid):
    global cnt_minus, cnt_one, cnt_zero
    if num == 1:
        if grid[0][0] == -1:
            cnt_minus += 1
        elif grid[0][0] == 0:
            cnt_zero += 1
        else:
            cnt_one += 1
        return

    is_same = True
    for i in range(num):
        if not is_same:
            break
        for j in range(num):
            if grid[i][j] != grid[0][0]:
                is_same = False
                break
                
    if not is_same:
        start_point = [(0, 0), (num // 3, 0), (num // 3 * 2, 0),
                       (0, num // 3), (num // 3, num // 3), (num // 3 * 2, num // 3),
                       (0, num // 3 * 2), (num // 3, num // 3 * 2), (num // 3 * 2, num // 3 * 2)]
        for x, y in start_point:
            temp = []
            for r in range(x, x + num // 3):
                temp_row = []
                for c in range(y, y + num // 3):
                    temp_row.append(grid[r][c])
                temp.append(temp_row)
            counting(num // 3, temp)
    else:
        if grid[0][0] == -1:
            cnt_minus += 1
        elif grid[0][0] == 0:
            cnt_zero += 1
        else:
            cnt_one += 1


N = int(input().strip())
table = [list(map(int, input().split())) for _ in range(N)]
cnt_minus = 0
cnt_zero = 0
cnt_one = 0
counting(N, table)
print(cnt_minus, cnt_zero, cnt_one, sep="\n")