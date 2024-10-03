def find_unique(numbers, size):
    # Create a dictionary to store the count of each number
    frequency = {}
    
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find the first unique element
    for num in numbers:
        if frequency[num] == 1:
            print("First unique element:", num)
            return

    print("No unique elements found.")
                             

# Get the size of the array
size = int(input("Enter size of array: "))
numbers = []  # Initialize an empty list
print("Enter the elements of the array:")

# Take input for each element of the array
for x in range(size):
    element = int(input(f"Element {x + 1}: "))
    numbers.append(element)  # Append each element to the list
    

find_unique(numbers, size)
    