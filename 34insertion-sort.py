'''
Insertion Sort Algorithm
 - Time Complexity: O(n^2)
 - Space Complexity: O(1)
 - Take an element from the unsorted list and add it to its correct position
 in the sorted list similar to playing cards. The user from it's left hand takes a
 card and places it in the right position in the right hand

'''

# program for insertion sort
def insertionSort(arr):
    n = len(arr)  # Get the length of the array
     
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
 
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
