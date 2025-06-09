'''
Linear Search
- This algorithm searches for a target value in a list by checking each element sequentially.
- Time complexity: O(n) in the worst case, where n is the number of elements in the list.
- Space complexity: O(1) since it uses a constant amount of space.
'''
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index of the found element
    return -1  # Return -1 if the target is not found
# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10, 55, 12, 99, 1, 0, 6, 4, 8, 2]
    target = input("Enter the element to search for: ")
    print("Original array:", arr)
    index = linear_search(arr, target)
    if index != -1:
        print(f"Element {target} found at index: {index}")
    else:
        print(f"Element {target} not found in the array.")