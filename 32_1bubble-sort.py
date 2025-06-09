'''
Bubble Sort:
 - Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
 - The pass through the list is repeated until the list is sorted.
 - Number of comparisons = n(n-1)/2
 - Best Case: O(n) when the array is already sorted
 - Worst Case: O(n^2) when the array is sorted in reverse order
 - Average Case: O(n^2) for random order

 - Space Complexity: O(1) as it requires no additional storage space
'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

nums = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:", bubble_sort(nums.copy()))
