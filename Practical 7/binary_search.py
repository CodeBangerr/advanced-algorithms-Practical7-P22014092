def binary_search_iterative(arr, target):
    """
    Searches for a target value in a sorted array using Binary Search.

    Parameters:
    arr: Sorted list to search in
    target: Value to find

    Returns:
    Index of the target value if found, otherwise -1
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # Check if target is at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1

        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # Target not found
    return -1


# Test the Binary Search
if __name__ == "__main__":
    arr = [8, 12, 31, 46, 57, 214]
    target = 31

    result = binary_search_iterative(arr, target)

    if result != -1:
        print(f"Found at index {result}")
    else:
        print("Not found")

    # Expected Output: Found at index 2