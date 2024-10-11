def insertion_sort(arr, size):
    for i in range(1, size):  # Correct the range to go from 1 to size-1
        temp = arr[i]  # Save the current element
        
        j = i - 1  # Start comparing with the element before current
        while j >= 0 and arr[j] > temp:  # Shift larger elements to the right
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = temp  # Place the temp element in its correct position
    
    print("Sorted array:", arr)  # Print the sorted array


# Get the size of the array
size = int(input("Enter the size of the array: "))
arr = []  # Initialize an empty array
print("Enter the elements of the array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element at index {x}: "))
    arr.append(element)  # Append each element to the list

insertion_sort(arr, size)
