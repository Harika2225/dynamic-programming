def merge_naive(arr1, arr2, n, m):
    # Step 1: Combine both arrays
    combined = arr1 + arr2

    # Step 2: Sort the combined array
    combined.sort()

    # Step 3: Copy first n elements to arr1
    for i in range(n):
        arr1[i] = combined[i]

    # Step 4: Copy remaining m elements to arr2
    for i in range(m):
        arr2[i] = combined[n + i]

arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]
merge_naive(arr1, arr2, len(arr1), len(arr2))

print("arr1:", arr1)  # ➤ [1, 2, 3, 4, 7]
print("arr2:", arr2)  # ➤ [8, 9, 10]
