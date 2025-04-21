# def find_duplicate(arr):
#     arr.sort()  # Sorting first
#     n = len(arr)
#     for i in range(n - 1):  # Loop till n-1 to avoid IndexError
#         if arr[i] == arr[i + 1]:
#             return arr[i]
def find_duplicate(arr):
    # Step 1: Use Floyd's Tortoise and Hare to find the intersection point
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Step 2: Find the entrance to the cycle
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow

arr = [1,3,4,2,2]
res=find_duplicate(arr)
print(res)