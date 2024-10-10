def bubble_sort(arr, size):
    for i in range(size - 1):  # Outer loop to control the number of passes
        swapped = False  # Track if a swap occurred during the pass
        for j in range(size - 1 - i):  # Inner loop to compare adjacent elements
            if arr[j] > arr[j + 1]:  # Swap if the current element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swapped = True  # Set swapped to True as a swap occurred
        if not swapped:  # If no swap occurred, array is already sorted
            break  # Break out of the loop early
            
    print("Sorted array:", arr)  # Print the sorted array


# Get the size of the array
size = int(input("Enter the size of the array: "))
arr = []  # Initialize an empty array
print("Enter the elements of the array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element at index {x}: "))
    arr.append(element)  # Append each element to the list

bubble_sort(arr, size)
Key Changes: