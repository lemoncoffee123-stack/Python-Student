import sys
input = sys.stdin.readline

def calculate(a, b, c):
    if b <= 2:
        return (a ** b) % c

    else:
        if b % 2 == 0:
            return (calculate(a, b//2, c)**2) % c
        else:
            return ((calculate(a, b//2, c)**2) * a) % c

A, B, C = map(int, input().split())
print(calculate(A, B, C))