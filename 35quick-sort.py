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