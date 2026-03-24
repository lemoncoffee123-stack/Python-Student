n, q = map(int, input().split())
word = input()
input_str = '#' + '#'.join(word) + '#'
word_len = len(input_str)
A = [0] * word_len
p = r = -1
for i in range(word_len):
    if r < i:
        A[i] = 0
    
    else:
        ii = 2 * p - i
        A[i] = min(r - i, A[ii])

    while i - A[i] - 1 >= 0 and i + A[i] + 1 < word_len and input_str[i - A[i] - 1] == input_str[i + A[i] + 1]:
        A[i] += 1

    if i + A[i] > r:
        r, p = i + A[i], i

for _ in range(q):
    a, b = map(int, input().split())
    mid = a + b - 1

    if A[mid] >= (b - a + 1):
        print("Yes")
    else:
        print("No")