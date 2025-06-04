'''
selection sort algorithm
- Number of comparisons: O(n^2)
- Number of swaps: O(n)
- A minimum element is selected from the unsorted part and swapped with the first unsorted element.
- Bubble sort performs multiple swaps, while selection sort performs only one swap per pass.
- Time complexity: O(n^2)
- Space complexity: O(1)
'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)