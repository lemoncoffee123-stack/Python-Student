T = int(input())

def find_dia(robot, dia):
    global cnt, dir_num
    x, y = robot
    nx, ny = dia

    if nx - x < 0:
        if ny - y < 0:
            cnt += direction[0][dir_num]
            dir_num = (dir_num + direction[0][dir_num]) % 4

        else:
            cnt += direction[1][dir_num]
            dir_num = (dir_num + direction[1][dir_num]) % 4

    else:
        if ny - y < 0:
            cnt += direction[2][dir_num]
            dir_num = (dir_num + direction[2][dir_num]) % 4
        else:
            cnt += direction[3][dir_num]
            dir_num = (dir_num + direction[3][dir_num]) % 4

    return

for test_case in range(1,T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    dia_idx = [0] * 11
    dia_cnt = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] != 0:
                dia_idx[table[i][j]] = (i, j)
                dia_cnt += 1

    dia_idx[0] = (0, 0)
    cnt = 0
    dir_num = 0
    direction = [[3, 2, 1, 3], [3, 3, 2, 1], [2, 1, 3, 3], [1, 3, 3, 2]]

    for i in range(1, dia_cnt + 1):
        find_dia(dia_idx[i - 1], dia_idx[i])

    print(f"#{test_case} {cnt}")