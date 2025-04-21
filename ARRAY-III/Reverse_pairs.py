class Solution(object):
    def reversePairs(self, nums):
        def merge_sort(arr, temp, left, right):
            cnt = 0
            if left < right:
                mid = (left + right) // 2
                
                cnt += merge_sort(arr, temp, left, mid)
                cnt += merge_sort(arr, temp, mid + 1, right)
                cnt += count_pairs(arr, left, mid, right)  # <- New step
                merge(arr, temp, left, mid, right)
            return cnt

        def count_pairs(arr, left, mid, right):
            cnt = 0
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and arr[i] > 2 * arr[j]:
                    j += 1
                cnt += (j - (mid + 1))
            return cnt

        def merge(arr, temp, left, mid, right):
            i = left       # index for left half
            j = mid + 1    # index for right half
            k = left       # index for merged array

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            for idx in range(left, right + 1):
                arr[idx] = temp[idx]

        n = len(nums)
        temp = [0] * n
        return merge_sort(nums, temp, 0, n - 1)