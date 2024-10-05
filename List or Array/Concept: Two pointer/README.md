# Intersection of Two Sorted Arrays Using Two-Pointer Approach


## Description
This script finds the intersection of two sorted integer arrays using the two-pointer approach. It is an efficient algorithm for finding common elements between two lists without additional space overhead. The two-pointer technique works well with *sorted arrays* and ensures that we traverse each array only once.

Given two sorted lists of integers, the function find_array_intersection_sorted returns a list containing elements that are common to both arrays, considering duplicate elements as well. For example, if both lists contain the number 2 twice, the result will include two 2s.


# Code Explanation
```python
def find_array_intersection_sorted(list1, list2, size1, size2):
    ptr1 = 0
    ptr2 = 0

    ans = []  # Initialize an empty list to store the intersection elements
    while ptr1 < size1 and ptr2 < size2:
        # If both elements are equal, add to the answer list and move both pointers
        if list1[ptr1] == list2[ptr2]:
            ans.append(list1[ptr1])
            ptr1 += 1
            ptr2 += 1

        # Move the pointer of the list with the smaller element
        elif list1[ptr1] < list2[ptr2]:
            ptr1 += 1  # Increment pointer for list1
        else:
            ptr2 += 1  # Increment pointer for list2

    print("Intersection of the two arrays:", ans)
```

## Input and Output

### Input:
- The user is prompted to enter the size of the first and second array.
- Elements are inputted into two separate lists: list1 and list2.

### Output:
- The function prints the intersection of the two arrays, considering duplicates.

## Example:
### Input:
```python
Enter size of array 1: 5
Enter the elements of the list 1:
1
2
2
3
4
Enter size of array 2: 4
Enter the elements of the list 2:
2
2
3
5
```

### Output
```python
Intersection of the two arrays: [2, 2, 3]
```


## Why Use the Two-Pointer Approach?

The two-pointer approach is ideal for finding intersections between two sorted arrays. Here's why it is effective:

- Efficiency:
    - Instead of using nested loops (which would have a time complexity of O(n×m)), the two-pointer approach allows us to iterate through both arrays in linear time O(n+m))

    - This is possible because the arrays are sorted, so we can efficiently move through each list without backtracking.

- Space Optimization:
    - No additional space, like hash maps or dictionaries, is required for storing counts. The only extra space used is for the output list.

- Handles Duplicates:
    - If both arrays contain duplicate elements, the two-pointer approach naturally handles them by only adding elements when both pointers point to the same value.


