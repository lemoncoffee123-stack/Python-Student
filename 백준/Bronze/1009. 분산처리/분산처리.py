t = int(input())
for tc in range(t):
    a, b = map(int, input().split())
    nums = []
    k = a % 10
    while True:
        if k in nums:
            break

        nums.append(k)
        k = (k * a) % 10
    c = b % len(nums) - 1
    if nums[c] == 0:
        print(10)
    else:
        print(nums[c])