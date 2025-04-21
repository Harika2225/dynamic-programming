def find_duplicate_and_missing(arr):
    n = len(arr)
    
    # Calculate sum1 (sum of 1 to N)
    sum1 = n * (n + 1) // 2
    # Calculate sum2 (sum of squares of 1 to N)
    sum2 = n * (n + 1) * (2 * n + 1) // 6
    # Initialize variables to store actual sum and sum of squares
    actual_sum = 0
    actual_sum_of_squares = 0
    
    # Traverse the array to compute actual sum and sum of squares
    for num in arr:
        actual_sum += num
        actual_sum_of_squares += num * num
    
    # The differences between expected and actual sums
    sum_diff = sum1 - actual_sum          # B - A
    sum_of_squares_diff = sum2 - actual_sum_of_squares  # B^2 - A^2
    
    # Now, we know that:
    # sum_diff = B - A
    # sum_of_squares_diff = B^2 - A^2 = (B - A)(B + A)
    # Thus:
    # sum_of_squares_diff = sum_diff * (B + A)
    
    # B + A can be found by dividing sum_of_squares_diff by sum_diff
    sum_of_A_and_B = sum_of_squares_diff // sum_diff
    
    # Now we have two equations:
    # B - A = sum_diff
    # B + A = sum_of_A_and_B
    
    # Solving these two equations:
    B = (sum_diff + sum_of_A_and_B) // 2
    A = B - sum_diff
    
    return A, B

# Example usage:
arr = [1, 4,3,2,5,5,6,7]
A, B = find_duplicate_and_missing(arr)
print("Duplicate Number:", A)
print("Missing Number:", B)
