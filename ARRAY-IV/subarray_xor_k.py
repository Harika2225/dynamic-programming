def subarraysWithXorK(nums, k):
    xr = 0
    cnt = 0
    mpp = {0: 1}  # Initialize with {0:1} to handle subarrays starting from index 0

    for num in nums:
        xr ^= num
        x = xr ^ k
        if x in mpp:
            cnt += mpp[x]
        if xr in mpp:
            mpp[xr] += 1
        else:
            mpp[xr] = 1

    return cnt

nums = [4, 2, 2, 6, 4]
k = 6
print(subarraysWithXorK(nums,k))