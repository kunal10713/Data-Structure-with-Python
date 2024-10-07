def find_peak_element(arr):
    # Initialize pointers
    start = 0
    end = len(arr) - 1

    # Run binary search until start and end pointers converge
    while start < end:
        mid = (start + end) // 2

        # Compare mid element with its right neighbor
        if arr[mid] < arr[mid + 1]:
            # Peak is on the right side, move start pointer
            start = mid + 1
        else:
            # Peak is on the left side (could be mid), move end pointer
            end = mid

    # When start == end, we have found the peak index
    return start


# Get the size of the array
size = int(input("Enter the size of the mountain array: "))
arr = []  # Initialize an empty array
print("Enter the elements of the mountain array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element at index {x}: "))
    arr.append(element)  # Append each element to the list

# Ensure the array is a valid mountain array (optional validation)

# Find the peak element index
peak_index = find_peak_element(arr)

# Print the peak element index and value
print(f"The peak element is at index: {peak_index} with value: {arr[peak_index]}")
