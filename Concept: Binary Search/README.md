# Binary Search Approach

## Problem Statement:
Given a **sorted array**, the goal is to find the position (index) of a specific element (key). If the element is found, the index is returned; otherwise, return `-1` indicating the element is not present in the array.

## Algorithm Explanation:

### 1. Initialization:
- Start by defining two pointers, `start` and `end`, representing the beginning and the end of the array.
- `start` is initialized to the first index of the array (`0`), and `end` is initialized to the last index (`size - 1`).

### 2. Finding the Middle Element:
- The algorithm calculates the middle index `mid` using the formula:
  \[
  \text{mid} = \frac{\text{start} + \text{end}}{2}
  \]
- This formula ensures that the `mid` index is always the integer value of the middle position of the current search range.

### 3. Comparison with Key:
- If the element at `arr[mid]` is equal to the `key`, the algorithm returns `mid` as the index of the key.
- If `key` is **greater** than `arr[mid]`, it means the key lies in the **right half** of the array. Update the `start` pointer to `mid + 1` to narrow down the search to the right half.
- If `key` is **less** than `arr[mid]`, it means the key lies in the **left half** of the array. Update the `end` pointer to `mid - 1` to narrow down the search to the left half.

### 4. Continue Searching:
- The algorithm repeats this process, continually narrowing down the search range by adjusting `start` and `end` pointers until:
  1. The key is found (`arr[mid] == key`).
  2. The search range becomes invalid (`start > end`), indicating that the key is not present in the array.

### 5. Key Not Found:
- If the key is not found after the loop ends, the function returns `-1` to indicate that the key does not exist in the array.

## Space and Time Complexity

### Time Complexity: 
- **O(log n)**  
  With each step, the search range is reduced by half, making binary search very efficient. For an array of size `n`, the number of iterations required is at most \( \log_2 n \).

### Space Complexity: 
- **O(1)**  
  Binary search uses constant extra space because it only requires a few additional variables (`start`, `end`, and `mid`), making it very space-efficient.
