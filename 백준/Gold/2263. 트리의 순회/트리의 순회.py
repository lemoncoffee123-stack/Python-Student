import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def preorder(in_st, in_ed, post_st, post_ed):
    if in_st > in_ed or post_st > post_ed:
        return

    root = postorder[post_ed]
    print(root, end=' ')

    idx = position[root]
    left_size = idx - in_st

    preorder(in_st, idx - 1, post_st, post_st + left_size - 1)

    preorder(idx + 1, in_ed, post_st + left_size, post_ed - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0] * (n + 1)
for i in range(n):
    position[inorder[i]] = i

preorder(0, n - 1, 0, n - 1)