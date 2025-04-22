# def longest_sequence(nums):
    # if not nums:
    #     return 0

    # nums.sort()  # Step 1
    # max_count = 1  # Step 2
    # count = 1      # Step 3

    # for i in range(1, len(nums)):  # Step 4
    #     if nums[i] == nums[i - 1]:  # Step 4a
    #         continue
    #     elif nums[i] == nums[i - 1] + 1:  # Step 4b
    #         count += 1
    #     else:  # Step 4c
    #         max_count = max(max_count, count)
    #         count = 1

    # return max(max_count, count)  # Step 5
# optimal:
def longest_sequence(nums):
    longest = 0
    num_set = set(nums)

    for n in num_set:
        if (n-1) not in num_set:
            length = 1
            while (n+length) in num_set:
                length += 1
            longest = max(longest, length)
    
    return longest

    
nums = [100,4,200,1,3,2]
print(longest_sequence(nums))