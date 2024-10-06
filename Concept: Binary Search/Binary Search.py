def binary_search(arr, size, key):
    # Initialize pointers
    start = 0
    end = size - 1

    # Run binary search until the pointers cross each other
    while start <= end:
        # Calculate the middle index
        mid = (start + end) // 2

        # Check if the middle element is the key
        if arr[mid] == key:
            return mid

        # If key is greater, ignore the left half
        elif key > arr[mid]:
            start = mid + 1

        # If key is smaller, ignore the right half
        else:
            end = mid - 1

    # If key is not found, return -1
    return -1


# Get the size of the array
size = int(input("Enter size of array: "))
arr = []  # Initialize an empty array
print("Enter the elements of the array (sorted in ascending order):")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element {x + 1}: "))
    arr.append(element)  # Append each element to the list

# Input the key to be searched
key = int(input("Enter the key to search for: "))

# Ensure the array is sorted (Optional, but necessary for binary search)
arr.sort()

# Perform binary search and print the result
index = binary_search(arr, size, key)
if index != -1:
    print(f"Index of key {key} is: {index}")
else:
    print(f"Key {key} not found in the array.")
