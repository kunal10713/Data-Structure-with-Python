def longest_subarray_with_k_unique(arr, k, size):
    left = 0
    right = 0
    unique_char = {}
    max_window = 0

    while right < size:
        # Add the character at 'right' to the dictionary or update its count
        if arr[right] in unique_char:
            unique_char[arr[right]] += 1
        else:
            unique_char[arr[right]] = 1

        # If there are less than k unique characters, move the 'right' pointer to expand the window
        if len(unique_char) < k:
            right += 1

        # If we have exactly k unique characters, calculate the window size
        elif len(unique_char) == k:
            max_window = max(max_window, right - left + 1)
            right += 1

        # If we have more than k unique characters, shrink the window from the left
        elif len(unique_char) > k:
            while len(unique_char) > k and left <= right:
                unique_char[arr[left]] -= 1
                
                if unique_char[arr[left]] == 0:
                    unique_char.pop(arr[left])   
                left += 1
                
            right += 1
    
    return max_window  # Return the result


# Input handling
size = int(input("Enter the size of array: "))  # Get the size of the array from user input
k = int(input("Enter the number of unique characters to present in the subarray: "))

# Take input for array elements from the user
arr = [input(f"Element at index {ele}: ") for ele in range(size)]

# Call the function and get the result
result = longest_subarray_with_k_unique(arr, k, size)

# Output the result
print(f"The size of the longest subarray with {k} unique characters is: {result}")