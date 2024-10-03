'''
Approach:
- Count Frequency: 
    First, count the frequency of each element using a dictionary.
- Check for Unique Occurrences: 
    Then, check if the number of occurrences (frequency) of each element is unique using a set data structure.
'''

def unique_occurrences(numbers):
    # Step 1: Create a frequency dictionary to count occurrences of each number
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Step 2: Create a set of frequencies to check for unique occurrences
    frequency_set = set(frequency.values())
    
    # Step 3: If the size of frequency_set is equal to the size of frequency dictionary values, return True
    # This means all frequencies are unique
    return len(frequency_set) == len(frequency.values())
       
                             

# Get the size of the numbersay
size = int(input("Enter size of numbersay: "))
numbers = []  # Initialize an empty list
print("Enter the elements of the numbersay:")

# Take input for each element of the numbersay
for x in range(size):
    element = int(input(f"Element {x + 1}: "))
    numbers.append(element)  # Append each element to the list
    

print(unique_occurrences(numbers))
    