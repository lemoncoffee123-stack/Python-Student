T = int(input())
for _ in range(T):
    word = input()
    n = 1
    result = 0
    for i in word:
        if i == 'O':
            result += n
            n += 1
        elif i == 'X':
            n = 1
    print(result)