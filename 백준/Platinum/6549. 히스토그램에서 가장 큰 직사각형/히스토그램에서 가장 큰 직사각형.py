import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def calculate(left, right):
    if right == left:
        return table[left]

    mid = (right + left) // 2
    height = max(calculate(left, mid), calculate(mid + 1, right))

    low = mid
    high = mid + 1
    h = min(table[low], table[high])
    height = max(height, h * 2)

    while left < low or high < right:
        if high < right and (low == left or table[low - 1] < table[high + 1]):
            high += 1
            h = min(h, table[high])

        else:
            low -= 1
            h = min(h, table[low])

        height = max(height, (high - low + 1) * h)

    return height


while True:
    a, *table = map(int, input().split())
    if a == 0:
        break
    result = calculate(0, a - 1)
    print(result)