def sort_zero_one(numbers, size):
    # Initialize two pointers: one starting from the beginning and the other from the end.
    ptr1 = 0
    ptr2 = size - 1

    # Continue while ptr1 is less than or equal to ptr2
    while ptr1 < ptr2:
        # Move ptr1 to the right if we see a 0 (it is already in the correct position)
        while numbers[ptr1] == 0:
            ptr1 += 1

        # Move ptr2 to the left if we see a 1 (it is already in the correct position)
        while numbers[ptr2] == 1:
            ptr2 -= 1

        # If ptr1 is still less than ptr2, swap the elements at ptr1 and ptr2
        if ptr1 < ptr2:
            # Swap elements at ptr1 and ptr2
            tmp = numbers[ptr1]
            numbers[ptr1] = numbers[ptr2]
            numbers[ptr2] = tmp
            ptr1 += 1
            ptr2 -= 1

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


sort_zero_one(numbers, size)