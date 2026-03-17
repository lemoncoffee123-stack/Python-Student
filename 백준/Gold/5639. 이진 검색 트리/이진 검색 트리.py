import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.read

def postorder(start, end):
    if start > end:
        return

    root = nodes[start]
    mid = start + 1

    while mid <= end:
        if nodes[mid] > root:
            break
        mid += 1

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(root)


lines = input().split()
if not lines:
    exit()

nodes = list(map(int, lines))
postorder(0, len(nodes) - 1)