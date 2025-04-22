# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 print("YES")
#                 print([i, j])
#                 return
#     print("NO")

# nums = [1, 2, 4, 5, 6, 8]
# target = 14

# two_sum(nums, target)

# Optimized version of the two_sum function using a hash map
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            print("YES")
            print([seen[complement], i])
            return
        seen[num] = i
    print("NO")

nums = [1, 2, 4, 5, 6, 8]
target = 14

two_sum(nums, target)
