def subarray_sum_k(nums, k):
    count = 0
    prefix_sum = 0
    prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 and count 1
    
    for num in nums:
        prefix_sum += num  # Update the running prefix sum
        if (prefix_sum - k) in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) is found
        if prefix_sum in prefix_sum_count:
            prefix_sum_count[prefix_sum] += 1  # Update the frequency of the current prefix sum
        else:
            prefix_sum_count[prefix_sum] = 1  # Initialize the frequency if the prefix sum is seen for the first time
    
    return count
    

k=2
nums = [1, 1, 1]
print(subarray_sum_k(nums, k))