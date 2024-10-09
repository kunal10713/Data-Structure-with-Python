# Book Allocation Problem

## Problem Description:
Given a list of books, each with a number of pages, the goal is to allocate books to a given number of students such that:

- Each student gets at least one book.
- Each student reads a contiguous set of books.
- The maximum number of pages assigned to a student is minimized.

The task is to find the minimum value of the maximum number of pages that can be assigned to a student.

## Constraints:
- The pages of any book should not be split between multiple students.
- The allocation must be contiguous, meaning that a student will only read a sequence of books that are consecutive in the list.

### Example:
Given the list of books: [12, 34, 67, 90] and 2 students, the optimal allocation is:
- Student 1: Books with pages [12, 34] → Total = 46 pages
- Student 2: Books with pages [67, 90] → Total = 157 pages

The answer is 157, as it is the minimum of the maximum pages a student has to read.



## Approach:
1. Binary Search Approach:
- We can use binary search to optimize the allocation of books. The idea is to minimize the maximum number of pages a student can read. This involves finding a range of possible values:

    - Start: 0 which is starting of the arr.
    - End: Sum of all pages in the list (sum(arr)).