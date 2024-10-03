def swap_alternative(numbers, size):
    # Initialize pointers for the first and second elements
    first = 0
    second = 1
    
    # Swap elements using a helper variable
    while second < size:
        helper = numbers[first]
        numbers[first] = numbers[second]
        numbers[second] = helper
        
        # Move to the next pair of elements
        first += 2
        second += 2
    
    # Print the modified list with swapped elements
    print("List after swapping alternate elements:", numbers)

# Get the size of the array
size = int(input("Enter size of array: "))
numbers = []  # Initialize an empty list
print("Enter the elements of the array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element {x + 1}: "))
    numbers.append(element)  # Append each element to the list

# Call the function to swap alternate elements
swap_alternative(numbers, size)
