def next_permutation(arr):
    n = len(arr)
    
    # Step 1: Find the first index i from the end where arr[i] < arr[i+1]
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    # Step 2: If found, find j such that arr[j] > arr[i] and j > i
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Step 3: Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]
    
    # Step 4: Reverse the part from i+1 to end
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

arr = [1, 2, 3]
print(next_permutation(arr))  # Output: [1, 3, 2]

arr = [3, 2, 1]
print(next_permutation(arr))  # Output: [1, 2, 3]

arr = [1, 1, 5]
print(next_permutation(arr))  # Output: [1, 5, 1]
