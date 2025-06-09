'''
Binary Search
- This algorithm searches for a target value in a sorted list by repeatedly dividing the search interval in half.
- Time complexity: O(log n) in the worst case, where n is the number of elements in the list.
- Space complexity: O(1) since it uses a constant amount of space.
- Can be implemented iteratively or recursively.
'''
#Iterative implementation of binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if arr[mid] == target:
            return mid  # Return the index of the found element
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Return -1 if the target is not found

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found

    mid = (left + right) // 2  # Find the middle index

    if arr[mid] == target:
        return mid  # Return the index of the found element
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)  # Search in the right half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)  # Search in the left half
# Example usage of recursive binary search
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 8, 9, 10, 12, 27, 38, 43, 55, 82, 99]  # Sorted array
    target = int(input("Enter the element to search for: "))
    print("Original array:", arr)
    #change the function call to binary_search for iterative search
    # Uncomment the next line to use iterative binary search
    # index = binary_search(arr, target)
    index = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if index != -1:
        print(f"Element {target} found at index: {index}")
    else:
        print(f"Element {target} not found in the array.")