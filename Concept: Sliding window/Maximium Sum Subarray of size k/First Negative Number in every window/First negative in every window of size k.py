def first_negative_subarray(arr, k, size):
    left = 0
    right = 0 

    negative_numbers = []  # List to store negative numbers in the current window
    result = []

    while right < size:
        if arr[right] < 0:
            negative_numbers.append(arr[right])  # Add negative number to the list

        if right - left + 1 < k:
            right += 1  # Expand the window to size k
        elif right - left + 1 == k:  # When the window size is exactly k
            # Print the first negative number or 0 if none exist
            if len(negative_numbers) == 0:
                result.append(0)  # No negative number found
            else:
                result.append(negative_numbers[0])  # First negative number in the window
            
            # Slide the window: check if the element being removed was a negative number
            if arr[left] == negative_numbers[0]:
                negative_numbers.pop(0)  # Remove it from the list of negative numbers

            left += 1  # Slide the window
            right += 1

    print(result)
                     


# Input handling
size = int(input("Enter the size of array: "))
k = int(input("Enter the size of subarray: "))

# Handle edge cases where subarray size is invalid
if k > size or k <= 0:
    print("Subarray size is invalid!")
else:
    arr = [int(input(f"Element at index {ele}: ")) for ele in range(size)]
    first_negative_subarray(arr, k, size)