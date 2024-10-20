def occurrence_of_anagram(arr, pattern, size):
    pattern_size = len(pattern)
    
    # Initialize the sliding window boundaries
    left = 0
    right = 0
    
    k = len(pattern)  # Window size should be equal to the pattern size
    
    # Dictionary to store frequency of characters in the pattern
    letters = {}
    
    # Build the frequency dictionary for the pattern
    for chr in pattern:
        if chr in letters:
            letters[chr] += 1
        else:
            letters[chr] = 1
    
    count = len(letters)  # Number of distinct characters in the pattern
    ans = []  # List to store the starting indices of anagrams
    
    # Traverse the array with the sliding window
    while right < size:
        # Reduce count if current character exists in the dictionary
        if arr[right] in letters:
            letters[arr[right]] -= 1
            if letters[arr[right]] == 0:
                count -= 1
        
        # Expand the window until its size equals 'k'
        if (right - left + 1) < k:
            right += 1
        
        elif (right - left + 1) == k:
            # If count becomes 0, it's a valid anagram
            if count == 0:
                ans.append(left)
            
            # Slide the window to the right
            if arr[left] in letters:
                letters[arr[left]] += 1
                if letters[arr[left]] > 0:
                    count += 1
            left += 1
            right += 1
    
    return ans


# Input handling
size = int(input("Enter the size of array: "))
pattern = input("Enter the pattern for which you want to find the anagrams: ")

# Handle edge cases where subarray size is invalid
if len(pattern) > size or len(pattern) <= 0:
    print("Subarray size is invalid!")
else:
    arr = [input(f"Element at index {ele}: ") for ele in range(size)]
    result = occurrence_of_anagram(arr, pattern, size)
    if result:
        print(f"Anagrams found at indices: {result}")
    else:
        print("No anagrams found.")
