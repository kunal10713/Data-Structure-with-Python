def search_pivot(arr):
    start = 0
    end = len(arr) - 1

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

def binary_search(arr, bin_start, bin_end, key):
    while bin_start <= bin_end:
        mid = (bin_start + bin_end) // 2

        # Check if the mid element is the key
        if arr[mid] == key:
            return mid
        # If key is smaller, ignore right half
        elif key < arr[mid]:
            bin_end = mid - 1
        # If key is larger, ignore left half
        else:
            bin_start = mid + 1

    return -1  # If key is not found

# Get the size of the array
size = int(input("Enter the size of the rotated array: "))
arr = []  # Initialize an empty array
print("Enter the elements of the rotated array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element at index {x}: "))
    arr.append(element)  # Append each element to the list

key = int(input("Enter the key that needs to be searched in the array: "))

# Find pivot element
pivot = search_pivot(arr)

# Determine in which part to search the key
if key >= arr[pivot] and key <= arr[size-1]:
    bin_start = pivot
    bin_end = size - 1
else:
    bin_start = 0
    bin_end = pivot - 1

# Search the key in the determined part
index = binary_search(arr, bin_start, bin_end, key)

# Print the result
if index != -1:
    print(f"Element {key} is at index {index}")
else:
    print(f"Element {key} not found in the array")
