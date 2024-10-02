def linear_search(numbers, number_to_search):
    for element in numbers:
        if element == number_to_search:  
            return True
        #index(): It returns the index of the element if found, rather than just checking for its presence.
        
    return False
    

size = int(input("Enter size of array: "))
numbers = []  # Initialize an empty list
print("Enter the elements of the array:")

for x in range(size):  # Use range(size) instead of range(0, size)
    element = int(input(f"Element {x + 1}: "))  # Prompt for each element
    numbers.append(element)  # Append the element to the list
    
number_to_search = int(input("Enter the number you want to search: "))

print(f"Is number {number_to_search} present in the arrray:  {linear_search(numbers, number_to_search)}")