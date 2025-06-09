'''
Merge Sort Algorithm
- This code implements the merge sort algorithm, which is a divide-and-conquer sorting algorithm.
- It recursively divides the array into halves, sorts each half, and then merges the sorted halves.
- Time complexity: O(n log n)
- Space complexity: O(n) due to the temporary arrays used for merging.
- Number of comparisons: O(n log n)
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)
def merge(left, right):
    merged = []
    i = j = 0

    # Merge the two halves while comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # If there are remaining elements in left, add them
    while i < len(left):
        merged.append(left[i])
        i += 1

    # If there are remaining elements in right, add them
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged
# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10, 55, 12, 99, 1, 0, 6, 4, 8, 2]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)