import sys
input = sys.stdin.readline

def quadtree(grid, num):
    if num == 1:
        if grid[0][0] == 0:
            return '0'
        else:
            return '1'

    is_same = True
    for i in range(num):
        if not is_same:
            break
        for j in range(num):
            if grid[i][j] != grid[0][0]:
                is_same = False
                break

    idx = [(0, 0), (0, num // 2), (num // 2, 0), (num // 2, num // 2)]

    if not is_same:
        tree = '('
        for x, y in idx:
            temp = []
            for i in range(x, x + num//2):
                temp_row = []
                for j in range(y, y + num//2):
                    temp_row.append(grid[i][j])
                temp.append(temp_row)

            tree = tree + str(quadtree(temp, num//2))
        tree = tree + ')'
        return tree

    else:
        if grid[0][0] == 0:
            return '0'
        else:
            return '1'


N = int(input().strip())
table = [list(map(int, input().strip())) for _ in range(N)]
result = quadtree(table, N)
print(result)