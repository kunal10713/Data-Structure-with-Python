def selection_sort(arr, size):
    for i in range(size - 1):
        min_index = i  # Set the first element as the minimum
        for j in range(i + 1, size):  # Find the minimum element in the remaining unsorted array
            if arr[j] < arr[min_index]:  # Compare current element with the current minimum
                min_index = j  # Update the index of the minimum element
        
        # Swap the found minimum element with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    print("Sorted array:", arr)  # Print the sorted array


# Get the size of the array
size = int(input("Enter the size of the array: "))
arr = []  # Initialize an empty array
print("Enter the elements of the array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element at index {x}: "))
    arr.append(element)  # Append each element to the list

selection_sort(arr, size)
