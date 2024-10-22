def largest_subarray_of_sum_k(arr, sum_k, size):
    left = 0  # Left boundary of the sliding window
    right = 0  # Right boundary of the sliding window
    max_window = 0  # Variable to store the size of the largest subarray
    current_sum = 0  # Variable to store the sum of the current window

    # Loop until the right boundary reaches the end of the array
    while right < size:
        current_sum += arr[right]  # Add the element at the right boundary to the current sum

        # If the current sum is less than the target sum, expand the window by moving the right boundary
        if current_sum < sum_k:
            right += 1

        # If the current sum equals the target sum, check if this window is the largest and expand
        elif current_sum == sum_k:
            # Update max_window to store the largest window size found so far
            max_window = max(max_window, right - left + 1)
            right += 1

        # If the current sum exceeds the target sum, shrink the window from the left
        elif current_sum > sum_k:
            # Continue shrinking the window until the current sum is less than or equal to the target sum
            while current_sum > sum_k and left <= right:
                current_sum -= arr[left]  # Subtract the element at the left boundary from current sum
                left += 1  # Move the left boundary to the right to shrink the window

            right += 1  # After shrinking, expand the window again by moving the right boundary

    return max_window  # Return the size of the largest subarray found

# Input handling
size = int(input("Enter the size of array: "))  # Get the size of the array from user input
sum_k = int(input("Enter the sum for which you want to find the subarray: "))  # Get the target sum from user input

# Take input for array elements from the user
arr = [int(input(f"Element at index {ele}: ")) for ele in range(size)]

# Call the function and get the result
result = largest_subarray_of_sum_k(arr, sum_k, size)

# Output the result
print(f"The size of the largest subarray with sum {sum_k} is: {result}")
