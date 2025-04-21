def merge(arr1, arr2, n, m):
    def next_gap(gap):
        if gap <= 1:
            return 0
        print(gap //2, gap %2)
        return (gap // 2) + (gap % 2)

    gap = next_gap(n + m)
    while gap > 0:
        # Compare in arr1
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        # Compare in both arrays
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Compare in arr2
        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

        gap = next_gap(gap)

# Example usage:
arr1 = [1, 4,8,9]
arr2 = [2, 3,10]
merge(arr1, arr2, len(arr1), len(arr2))

print("arr1:", arr1)
print("arr2:", arr2)