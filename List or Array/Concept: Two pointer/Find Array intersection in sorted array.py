import sys

def find_array_intersection_sorted(list1, list2, size1, size2):
    ptr1 = 0
    ptr2 = 0

    ans = []
    while(ptr1 < size1 and ptr2 < size2):
        if(list1[ptr1] == list2[ptr2]):
            ans.append(list1[ptr1])
            list2[ptr2] = sys.maxint
            ptr1 += 1
            ptr2 += 1
            
        if(list1[ptr1] < list2[ptr2]):
            ptr1 += 1
            continue
        
        if(list1[ptr1] > list2[ptr2]):
            ptr2 += 1
            continue
    
    print(ans)
    

# Get the size of the array
size1 = int(input("Enter size of array 1: "))
list1 = []  # Initialize an empty list
list2 = []  # Initialize an empty list

print("Enter the elements of the list 1, Make sure input is sorted:")

# Take input for each element of array 1
for x in range(size1):
    element = int(input(f"Element {x + 1}: "))
    list1.append(element)  # Append each element to the list

size2 = int(input("Enter size of array 2: Make sure input is sorted: "))

print("Enter the elements of the list 2:")

# Take input for each element of array 2
for x in range(size2):
    element = int(input(f"Element {x + 1}: "))
    list2.append(element)  # Append each element to the list

# Call the function to find and print the intersection
find_array_intersection_sorted(list1, list2, size1, size2)
