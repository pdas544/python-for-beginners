'''
Quick Sort Algorithm
- It is a divide-and-conquer algorithm.
- It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
- The sub-arrays are then sorted recursively.
- Time complexity: O(n log n) on average, O(n^2) in the worst case (when the smallest or largest element is always chosen as the pivot).
- Space complexity: O(log n) due to recursive stack space.
- Number of comparisons: O(n log n) on average, O(n^2) in the worst case.
- The choice of pivot can significantly affect performance; common strategies include choosing the first element, the last element, or the median.
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
        left = [x for x in arr if x < pivot]  # Elements less than pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to pivot
        right = [x for x in arr if x > pivot]  # Elements greater than pivot
        return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11, 90, 45, 78, 34, 56, 23]
    print("Original array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)

'''
Recursive Quick Sort Algorithm
'''
def quick_sort_recursive(arr, low, high):
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1  # Pointer for the smaller element
    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than or equal to pivot
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i + 1
    return i + 1  # Return the partitioning index
# Example usage of recursive quick sort
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11, 90, 45, 78, 34, 56, 23]
    print("Original array:", arr)
    quick_sort_recursive(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)