# Intersection of Two Arrays

## Description
This script defines a function find_array_intersection that finds the intersection of two integer arrays. Given two lists of integers, the function returns a list containing elements that are common to both arrays, accounting for duplicate elements as well. For example, if both lists contain the number 2 twice, the result should include two 2s.


# Code Explanation
```python
def find_array_intersection(list1, list2):
    # Create dictionaries to store the count of each number in both lists
    dict1 = {}
    dict2 = {}
    
    ans = []  # List to store the intersection elements
    
    # Count the occurrences of each element in the first list
    for elem_list1 in list1:
        if elem_list1 in dict1:
            dict1[elem_list1] += 1
        else:
            dict1[elem_list1] = 1
            
    # Count the occurrences of each element in the second list
    for elem_list2 in list2:
        if elem_list2 in dict2:
            dict2[elem_list2] += 1
        else:
            dict2[elem_list2] = 1
            
    # Find the intersection by comparing elements in both dictionaries
    for key in dict1:
        if key in dict2:  # Check if the element is present in both dictionaries
            min_count = min(dict1[key], dict2[key])  # Get the minimum count of the element in both lists
            ans.extend([key] * min_count)  # Add 'min_count' occurrences of the element to the result list
    
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


## Why Use extend() Instead of append()?
The function uses the extend() method to add multiple occurrences of an element to the result list. This is necessary because append() would add the list itself as a single element, rather than its individual elements.

## For example:

```python
ans = []
ans.append([2] * 2)  # This would add [2, 2] as a single element in the list, resulting in: [[2, 2]]
```

### Using extend():
```python
ans.extend([2] * 2)  # This adds the individual elements 2, 2 to the list, resulting in: [2, 2]
```

### append() vs. extend():
- append():
    -  Adds the object passed as a single element.
    - If you pass a list, it adds that list as one element. So, using ans.append([elem] * min_count) would add a list of repeated elements (e.g., [2, 2]) as a single item in the ans list, resulting in [[2, 2]].

- extend():
    - Iterates over the iterable and adds each element individually to the list.
    - This results in a flat list of repeated elements, which is the desired output format.