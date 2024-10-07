def binary_search_first(arr, size, key):
    start = 0
    end = size - 1
    first_occurrence = -1  # Initialize to -1 to indicate key not found

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            first_occurrence = mid  # Store the index
            end = mid - 1  # Continue searching in the left half
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return first_occurrence


def binary_search_last(arr, size, key):
    start = 0
    end = size - 1
    last_occurrence = -1  # Initialize to -1 to indicate key not found

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            last_occurrence = mid  # Store the index
            start = mid + 1  # Continue searching in the right half
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return last_occurrence


# Get the size of the array
size = int(input("Enter size of array: "))
arr = []  # Initialize an empty array
print("Enter the elements of the array (sorted in ascending order):")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element at index {x}: "))
    arr.append(element)  # Append each element to the list

# Input the key to be searched
key = int(input("Enter the key to search for: "))

# Ensure the array is sorted (Optional, but necessary for binary search)
arr.sort()

# Perform binary search for first and last occurrences
first_index = binary_search_first(arr, size, key)
last_index = binary_search_last(arr, size, key)

# Print the results
if first_index != -1:
    print(f"First occurrence of key {key} is at index: {first_index}")
    print(f"Last occurrence of key {key} is at index: {last_index}")
else:
    print(f"Key {key} not found in the array.")
