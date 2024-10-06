def sort_zero_one_two(numbers, size):
    # Initialize three pointers
    ptr0 = 0  # Pointer for the next position of 0
    ptr1 = 0  # Current element pointer
    ptr2 = size - 1  # Pointer for the next position of 2

    # Continue while ptr1 is less than or equal to ptr2
    while ptr1 <= ptr2:
        if numbers[ptr1] == 0:
            # Swap if the current element is 0
            numbers[ptr0], numbers[ptr1] = numbers[ptr1], numbers[ptr0]
            ptr0 += 1
            ptr1 += 1
        elif numbers[ptr1] == 1:
            ptr1 += 1  # Just move the pointer for 1s
        else:  # numbers[ptr1] == 2
            # Swap if the current element is 2
            numbers[ptr1], numbers[ptr2] = numbers[ptr2], numbers[ptr1]
            ptr2 -= 1  # Reduce the size of the array for 2s

    # Print the sorted array
    print(numbers)   
            
# Get the size of the array
size = int(input("Enter size of array: "))
numbers = []  # Initialize an empty list
print("Enter the elements of the array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element {x + 1}: "))
    numbers.append(element)  # Append each element to the list

sort_zero_one_two(numbers, size)
