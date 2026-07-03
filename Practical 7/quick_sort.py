def quick_sort(arr, low, high):
    """
    Sorts an array using the Quick Sort algorithm (Divide and Conquer).

    Parameters:
    arr: List of elements to be sorted
    low: Starting index (0 for full array)
    high: Ending index (len(arr) - 1 for full array)
    """
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort the left and right subarrays
        quick_sort(arr, low, pivot_index - 1)  # Left of pivot
        quick_sort(arr, pivot_index + 1, high)  # Right of pivot


def partition(arr, low, high):
    """
    Partitions the array using the last element as pivot.
    Places the pivot in its correct sorted position.

    Parameters:
    arr: List to be partitioned
    low: Starting index
    high: Ending index (pivot is at this position)

    Returns:
    The final position of the pivot element
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]

    # i tracks the position of the last element smaller than pivot
    i = low - 1

    # Traverse through all elements
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment i and swap
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the pivot's final index
    return i + 1


def quick_sort_wrapper(arr):
    """
    Wrapper function to make Quick Sort easier to call.

    Parameters:
    arr: List to be sorted

    Returns:
    Sorted list (sorts in-place)
    """
    quick_sort(arr, 0, len(arr) - 1)
    return arr


# Test the Quick Sort implementation
if __name__ == "__main__":
    # Input array
    arr = [214, 12, 46, 57, 31, 8]
    print("Original array:", arr)

    # Sort the array using Quick Sort
    sorted_arr = quick_sort_wrapper(arr.copy())

    # Display the result
    print("Sorted array:", sorted_arr)

    # Expected output: [8, 12, 31, 46, 57, 214]