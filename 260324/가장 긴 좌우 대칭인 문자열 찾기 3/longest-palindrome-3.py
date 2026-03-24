n, c = input().split()
word = input()
input_str = "#" + "#".join(word) + "#"
str_len = len(input_str)
A = [0] * str_len
p = r = -1

for i in range(str_len):
    if r < i:
        A[i] = 0
    
    else:
        ii = 2 * p - i
        A[i] = min(r - i, A[ii])
    
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < str_len and input_str[i - A[i] - 1] == input_str[i + A[i] + 1]:
        if input_str[i -A[i] - 1] == c or input_str[i + A[i] + 1] == c:
            break

        A[i] += 1

    if i + A[i] > r:
        r, p = i + A[i], i

print(max(A))