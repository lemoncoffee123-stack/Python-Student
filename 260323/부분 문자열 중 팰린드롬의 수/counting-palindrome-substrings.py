word = input()
input_str = "#" + "#".join(word) + "#"
n = len(input_str)

A = [1] * n
p = r = -1

for i in range(n):
    if r < i:
        A[i] = 0
    
    else:
        ii = 2 * p - i
        A[i] = min(r - i, A[ii])

    while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and input_str[i - A[i] - 1] == input_str[i + A[i] + 1]:
        A[i] += 1

    if A[i] + i > r:
        r, p = i + A[i], i

result = 0
for val in A:
    result += (val + 1) // 2
print(result)