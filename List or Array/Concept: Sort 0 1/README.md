# Sort 0s and 1s Using Two-Pointer Approach

This repository provides an implementation of an efficient algorithm to sort an array containing only 0s and 1s using the two-pointer approach. The solution is designed to minimize the number of operations and achieve linear time complexity, O(n).

# Overview
The sort_zero_one function takes an array of size n containing only 0s and 1s and sorts it in linear time using the two-pointer technique. The goal is to place all 0s on the left side and all 1s on the right side of the array. This approach is simple yet efficient and avoids the need for extra space or complex sorting algorithms


## Approach
We use a two-pointer technique to traverse the array from both ends simultaneously:
- Pointer ptr1 starts from the beginning of the array.
- Pointer ptr2 starts from the end of the array.
The algorithm iteratively moves the pointers toward each other, swapping values when necessary. This results in sorting the array in a single pass.


## Steps Involved
- Initialize Pointers:
    - ptr1 is initialized at index 0.
    - ptr2 is initialized at index size - 1 (last element of the array).

- Move Pointers:
    - Increment ptr1 until a 1 is encountered.
    - Decrement ptr2 until a 0 is encountered..

- Swap Values:
    - If ptr1 < ptr2, swap the values at ptr1 and ptr2 so that a 0 moves to the left and a 1 moves to the right.

- Repeat Until Sorted:
    - Continue this process until ptr1 and ptr2 cross each other, indicating that the array is fully sorted.


## Complexity Analysis
### Time Complexity: O(n)
- Each element is visited at most once by ptr1 or ptr2. Hence, the number of operations is directly proportional to the size of the array, n.

### Space Complexity: O(1)

- The algorithm uses only a constant amount of extra space (two pointers and a temporary variable), irrespective of the size of the array.