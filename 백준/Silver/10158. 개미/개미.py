import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input().strip())

x = (p + t) % (2 * w)
if x > w:
    x = 2 * w - x
y = (q + t) % (2 * h)
if y > h:
    y = 2 * h - y

print(x, y)