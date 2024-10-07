
# Finding the Peak Element in a Mountain Array

## Problem Statement:

Given an array representing a mountain, where elements first increase to a peak and then decrease, the goal is to find the index of the peak element using binary search. The peak element is defined as the element that is greater than its neighbors. This problem is an application of binary search on a special array structure.


### Understanding the else Logic in Peak Finding Algorithm
In the binary search-based peak finding algorithm for a mountain array, the else clause handles the scenario when the current middle element is greater than the next element. Let's dive into why this logic works and what it signifies.

### Recap of the Approach:
The main idea of the algorithm is to determine whether to move the start pointer or the end pointer based on the comparison of arr[mid] and arr[mid + 1]. The algorithm works on the principle that a mountain array increases to a peak and then decreases.

### Here's the critical part of the code we're focusing on:
```python
if arr[mid] < arr[mid + 1]:
    # If the middle element is less than the next element, 
    # it means we are in the increasing part of the array.
    start = mid + 1
else:
    # If the middle element is greater than or equal to the next element,
    # it means we are in the decreasing part of the array.
    end = mid
```
### Analysis of the else Block:

#### Condition Explanation:

- If the current middle element arr[mid] is greater than or equal to the next element arr[mid + 1], it 
indicates that we are in the decreasing part of the mountain array.
- This condition helps us narrow down the search to the left side of the array, as the peak must be in this range.

#### Why Move end to mid?

- By setting end = mid, we effectively eliminate the right half of the current search space and focus on the left half.
- This adjustment is safe because arr[mid] could still be the peak. If arr[mid] > arr[mid + 1], then mid itself might be the peak (since it's greater than its right neighbor).
- Therefore, we don't skip over mid by setting end = mid - 1 as we do in typical binary search, because we need to ensure mid is not the peak before eliminating it.

## Time and Space Complexity:
### Time Complexity: 
- O(logn) - The array is divided into half at each step, making the time complexity logarithmic.
### Space Complexity: 
- O(1) - Only a few additional variables (start, end, mid) are used.
