import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))
nums.sort()

result = float('inf')
i, j = 0, N - 1
while i < j:
    diff = nums[i] + nums[j]

    if abs(diff) < result:
        result = abs(diff)
        result_num1, result_num2 = nums[i], nums[j]

    if result == 0:
        break

    if diff > 0:
        j -= 1

    else:
        i += 1
print(result_num1, result_num2)