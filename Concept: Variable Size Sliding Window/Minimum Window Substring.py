def minimum_window_subarray(s, sub_string, size):
    sub_string_map = {}
    
    # Create a frequency map for the characters in sub_string
    for char in sub_string:
        if char in sub_string_map:
            sub_string_map[char] += 1
        else:
            sub_string_map[char] = 1

    
    left = 0
    right = 0
    count_of_required_char = len(sub_string_map)  # Total unique characters to be matched
    min_window = float('inf')  # Initialize to infinity to find the minimum window
    start_index = -1  # To store the starting index of the minimum window
    
    # Iterate with the right pointer expanding the window
    while right < size:
        # Decrease the count of the current character if it's in sub_string_map
        if s[right] in sub_string_map:
            sub_string_map[s[right]] -= 1
            # If a required character count reaches 0, it means we have all its occurrences in the window
            if sub_string_map[s[right]] == 0:
                count_of_required_char -= 1

        # Try to minimize the window size when all characters are matched
        while count_of_required_char == 0:
            window_size = right - left + 1
            min_window = min(min_window, window_size)
            start_index = left  # Track where the minimum window starts

            # Now try to shrink the window from the left
            if s[left] in sub_string_map:
                sub_string_map[s[left]] += 1
                # If a character goes above its required count, increase the required character count
                if sub_string_map[s[left]] > 0:
                    count_of_required_char += 1

            left += 1  # Move the left pointer to shrink the window

        right += 1  # Move the right pointer to expand the window

    # Return the minimum window length or -1 if no valid window is found
    return min_window 

# Input handling
size = int(input("Enter the size of the string: "))  # Get the size of the string from user input
sub_string = input("Enter the substring: ")

# Take input for string elements from the user
s = input("Enter the string: ")

# Call the function and get the result
result = minimum_window_subarray(s, sub_string, size)

# Output the result
print(f"The size of the minimum window containing all characters of the substring is: {result}")
