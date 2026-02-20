import sys
input = sys.stdin.readline

table = list(input().strip())
cnt = 0
is_minus = False
num = ''
for i in table:
    if i.isdigit():
        num = num + i
    else:
        if not is_minus:
            cnt += int(num)
            num = ''
        else:
            cnt -= int(num)
            num = ''

        if i == '-':
            is_minus = True
else:
    if not is_minus:
        cnt += int(num)
    else:
        cnt -= int(num)
print(cnt)