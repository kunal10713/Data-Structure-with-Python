def sum_list(my_list):
    total = 0  
    for element in my_list:
        total += element 

    return total
    

size = int(input("Enter size of array: "))
numbers = []  # Initialize an empty list
print("Enter the elements of the array:")

for x in range(size):  # Use range(size) instead of range(0, size)
    element = int(input(f"Element {x + 1}: "))  # Prompt for each element
    numbers.append(element)  # Append the element to the list

print("Sum of numbers in the list:", sum_list(numbers))
