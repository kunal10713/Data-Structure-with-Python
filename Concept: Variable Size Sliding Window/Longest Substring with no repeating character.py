def longest_subarray_with_no_repeating_char(arr, size): 
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
        
        # Condition to shrink the window if there are repeating characters
        if unique_char[arr[right]] > 1:
            # If the character at 'right' has a count > 1, it's a repeating character
            while unique_char[arr[right]] > 1:  # Shrink window until no repeating character
                unique_char[arr[left]] -= 1
                if unique_char[arr[left]] == 0:  # If count reaches 0, remove the character from the dictionary
                    del unique_char[arr[left]]
                left += 1
        
        # Condition to calculate the max window when all characters in the window are unique
        if unique_char[arr[right]] == 1:
            max_window = max(max_window, right - left + 1)  # Update max window size if needed
        
        # Move the 'right' pointer to expand the window
        right += 1
    
    return max_window  # Return the result


# Input handling
size = int(input("Enter the size of array: "))  # Get the size of the array from user input

# Take input for array elements from the user
arr = [input(f"Element at index {ele}: ") for ele in range(size)]

# Call the function and get the result
result = longest_subarray_with_no_repeating_char(arr, size)

# Output the result
print(f"The size of the longest subarray with no repeating characters is: {result}")
