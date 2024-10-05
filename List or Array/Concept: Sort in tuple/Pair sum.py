def pair_sum(numbers, target_sum, size):
    ans = []
    
    # Iterate over the array with two pointers, similar to nested loops
    for ptr1 in range(size):
        for ptr2 in range(ptr1 + 1, size):
            if numbers[ptr1] + numbers[ptr2] == target_sum:
                # Store pairs as tuples
                ans.append((min(numbers[ptr1], numbers[ptr2]), max(numbers[ptr1], numbers[ptr2])))
    
    # Sort the pairs based on the first value (and second value if first are equal)
    ans.sort()

    # Print the result
    print("Pairs in non-decreasing order based on the first value:")
    for pair in ans:
        print(pair)

# Get the size of the array
size = int(input("Enter size of array: "))
numbers = []  # Initialize an empty list
print("Enter the elements of the array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element {x + 1}: "))
    numbers.append(element)  # Append each element to the list

target_sum = int(input("Enter the sum which we need to find the pair: "))
pair_sum(numbers, target_sum, size)