import sys, bisect
sys.setrecursionlimit(10*6)
input = sys.stdin.readline


def make_team(num_list, start, visited, num_sum, group):
    for i in range(start, len(num_list)):
        if not visited[i]:
            visited[i] = True
            num_sum += num_list[i]
            group.append(num_sum)

            make_team(num_list, i + 1, visited, num_sum, group)

            visited[i] = False
            num_sum -= num_list[i]

    return group

N, C = map(int, input().split())
nums = list(map(int, input().split()))
mid_num = N // 2
num_list_A, num_list_B = nums[:mid_num], nums[mid_num:]
visited_A, visited_B = [False] * len(num_list_A), [False] * len(num_list_B)
group_A, group_B = make_team(num_list_A, 0, visited_A, 0, [0]), make_team(num_list_B, 0, visited_B, 0, [0])
group_B.sort()

result = 0
for a in group_A:
    if a <= C:
        count = bisect.bisect_right(group_B, C - a)
        result += count

print(result)