def quick_sort(arr):
    """Main function to sort an array using the Quicksort algorithm."""
    if len(arr) <= 1:
        return arr  # Base case: array with 0 or 1 element is already sorted
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to pivot
        right = [x for x in arr if x > pivot]  # Elements greater than pivot
        
        # Recursively sort the left and right subarrays and combine
        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [-1000, -100, -10, -1, 0, 0.5, 10, 50, 99, 100, 1000]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
