def max_sum_subarray(arr, k, size):
    left = 0
    right = 0
    
    current_sum = 0  
    max_sum = float('-inf')  # Use -infinity to handle negative numbers correctly
    
    while right < size:
        current_sum += arr[right]
        
        if right - left + 1 < k:
            right += 1
        elif right - left + 1 == k:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[left]  # Slide the window by removing the leftmost element
            left += 1
            right += 1
    
    print(max_sum)

# Input handling
size = int(input("Enter the size of array: "))
k = int(input("Enter the size of subarray: "))

# Handle edge cases where subarray size is invalid
if k > size or k <= 0:
    print("Subarray size is invalid!")
else:
    arr = [int(input(f"Element at index {ele}: ")) for ele in range(size)]
    max_sum_subarray(arr, k, size)
