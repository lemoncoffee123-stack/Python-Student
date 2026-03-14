class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

MAX_N = 250001
nodes = [None] * MAX_N

def connect(start, end):
    if start is not None:
        start.next = end

    if end is not None:
        end.prev = start

def swapSubarray(a, b, c, d):
    after_prevA = c.prev
    after_nextB = d.next

    after_prevC = a.prev
    after_nextD = b.next

    if b.next == c:
        after_prevA = d
        after_nextD = a

    if d.next == a:
        after_nextB = c
        after_prevC = b

    connect(after_prevA, a)
    connect(b, after_nextB)

    connect(after_prevC, c)
    connect(d, after_nextD)


N = int(input())
Q = int(input())
for i in range(1, N + 1):
    nodes[i] = Node(i)

for i in range(1, N):
    connect(nodes[i], nodes[i + 1])

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    swapSubarray(nodes[a], nodes[b], nodes[c], nodes[d])
        
curr = nodes[1]
while curr.prev:
    curr = curr.prev

while curr:
    print(curr.data, end=" ")
    curr = curr.next