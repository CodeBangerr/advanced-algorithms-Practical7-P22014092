def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm (Divide and Conquer).

    Parameters:
    arr: List of elements to be sorted

    Returns:
    Sorted list
    """
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide: Find the middle point
    mid = len(arr) // 2

    # Conquer: Recursively sort the left and right halves
    left = merge_sort(arr[:mid])  # Sort left half
    right = merge_sort(arr[mid:])  # Sort right half

    # Combine: Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.

    Parameters:
    left: Sorted list (left half)
    right: Sorted list (right half)

    Returns:
    Merged sorted list
    """
    result = []
    i, j = 0, 0  # Pointers for left and right arrays

    # Compare elements from left and right and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from left (if any)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from right (if any)
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Test the Merge Sort implementation
if __name__ == "__main__":
    # Input array
    arr = [214, 12, 46, 57, 31, 8]
    print("Original array:", arr)

    # Sort the array using Merge Sort
    sorted_arr = merge_sort(arr)

    # Display the result
    print("Sorted array:", sorted_arr)

    # Expected output: [8, 12, 31, 46, 57, 214]