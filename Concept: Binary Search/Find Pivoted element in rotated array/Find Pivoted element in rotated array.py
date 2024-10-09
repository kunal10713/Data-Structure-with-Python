def pivot_element(arr):
    # Initialize pointers
    start = 0
    end = len(arr) - 1

    # If the array is not rotated, return the first element as the pivot
    if arr[start] <= arr[end]:
        return start

    # Run binary search until start and end pointers converge
    while start < end:
        mid = (start + end) // 2

        # If mid element is greater than or equal to the first element,
        # the pivot is in the right half, so move start to mid + 1
        if arr[mid] >= arr[0]:
            start = mid + 1
        # Otherwise, the pivot is in the left half, so move end to mid
        else:
            end = mid

    # Start will point to the pivot element
    return start


# Get the size of the array
size = int(input("Enter the size of the rotated array: "))
arr = []  # Initialize an empty array
print("Enter the elements of the rotated array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element at index {x}: "))
    arr.append(element)  # Append each element to the list

# Find the pivot element index
pivot_index = pivot_element(arr)

# Print the pivot element index and value
print(f"The pivot element is at index: {pivot_index} with value: {arr[pivot_index]}")
