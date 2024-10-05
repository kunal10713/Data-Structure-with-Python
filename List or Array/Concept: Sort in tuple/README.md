# Pair Sum Finder

## Description
This script defines a function `pair_sum` that identifies all unique pairs of integers within a list that add up to a specified target sum. The pairs are returned in non-decreasing order based on their first element.

## Code Explanation
```python
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
```

## Sort in tuple:
- Tuple Storage: By storing pairs as tuples, you maintain their relationship.
- Sorting: The sort() method is used to sort the list of tuples. By default, tuples are sorted by their first element, and if they are equal, then by their second element.
- Output: The final print statement will display pairs in the desired non-decreasing order.

## Time Complexity
- The overall time complexity is O(n^2) due to the nested loops, where  n is the number of elements in the input list.
- Sorting the pairs would add an additional O(klogk), where k is the number of valid pairs found.