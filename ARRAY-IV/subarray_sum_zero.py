def subarray_sum_zero(nums, k):
    max_len = 0
    prefix_sum = 0
    sum_index_map = {0: -1}  # Initialize with prefix sum 0 and count 1
    
    for i, num in enumerate(nums):
        prefix_sum += num  
        if prefix_sum in sum_index_map:
            max_len = max(max_len, i - sum_index_map[prefix_sum])  # Update max_len if the prefix sum is found
        else:
            sum_index_map[prefix_sum] = i  # Store the index of the first occurrence of the prefix sum
    
    return max_len
    
n = 6
nums = [9, -3, 3, -1, 6, -5]
print(subarray_sum_zero(nums, n))