def find_array_intersection(list1, list2):
    # Dictionaries to store the frequency of elements in both lists
    frequency1 = {}
    frequency2 = {}

    # Count frequencies of each element in list1
    for elem in list1:
        if elem in frequency1:
            frequency1[elem] += 1
        else:
            frequency1[elem] = 1

    # Count frequencies of each element in list2
    for elem in list2:
        if elem in frequency2:
            frequency2[elem] += 1
        else:
            frequency2[elem] = 1

    # List to store the intersection with duplicates
    ans = []

    # Find the intersection by checking minimum frequency in both dictionaries
    for elem in frequency1:
        if elem in frequency2:
            # Include the element in the result as many times as it appears in both lists
            min_count = min(frequency1[elem], frequency2[elem])
            ans.extend([elem] * min_count)

    # Print or return the intersected elements with duplicates
    print("Intersection of the arrays:", ans)


# Get the size of the array
size1 = int(input("Enter size of array 1: "))
list1 = []  # Initialize an empty list
list2 = []  # Initialize an empty list

print("Enter the elements of the list 1:")

# Take input for each element of array 1
for x in range(size1):
    element = int(input(f"Element {x + 1}: "))
    list1.append(element)  # Append each element to the list

size2 = int(input("Enter size of array 2: "))

print("Enter the elements of the list 2:")

# Take input for each element of array 2
for x in range(size2):
    element = int(input(f"Element {x + 1}: "))
    list2.append(element)  # Append each element to the list

# Call the function to find and print the intersection
find_array_intersection(list1, list2)


