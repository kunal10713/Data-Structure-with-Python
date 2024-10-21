# Bubble Sort Algorithm


## Overview
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm is named for the way larger elements "bubble" to the top of the list.

### How It Works
Given an array of integers, Bubble Sort sorts the array in ascending order. The algorithm involves two loops:
- The Outer Loop (for i in range(size - 1)) controls the number of passes through the array.
- The Inner Loop (for j in range(size - 1 - i)) compares adjacent elements in each pass and swaps them if needed.

### Why Use size - 1 and size - 1 - i?
#### Outer Loop (size - 1): 
- In bubble sort, each pass through the array places the next largest element in its final position. If there are n elements in the array, the sorting process requires at most n - 1 passes.
- This is because after the first pass, the largest element is already at its correct position. After the second pass, the second largest element is at its position, and so on. Thus, the final pass does not need to be performed as it only needs to run n - 1 passes to ensure sorting.


#### Inner Loop (size - 1 - i): 
- After each pass, the largest element in the unsorted portion of the array "bubbles up" to its correct position at the end of the array. Therefore, there is no need to include the last element in subsequent passes because it is already in its correct place.
- Thus, as i (the outer loop index) increases with each pass, the effective range of the inner loop decreases by 1 (using size - 1 - i), since the last i elements are already sorted.



### Complexity Analysis:
#### Time Complexity:
- Worst-case: O(n²)
- Best-case: O(n) when the array is already sorted (due to the swapped flag optimization).

#### swapped Flag:
- The flag swapped is introduced to keep track of whether any swaps were made during a pass.
- If no swaps are made (swapped = False), it means the array is already sorted, and we can exit the loop early using break.


#### Space Complexity:
- O(1) as bubble sort sorts the array in place without using any extra space.


#### When to Use Selection Sort:
- Small Arrays: Similar to Bubble Sort, Selection Sort works well with small datasets.
- Low Swap Cost: Selection Sort makes at most n swaps, which is optimal if swapping elements is expensive or if you are dealing with large records.
- Memory Constraints: Selection Sort is a good option when memory usage is a concern, as it has O(1) space complexity.