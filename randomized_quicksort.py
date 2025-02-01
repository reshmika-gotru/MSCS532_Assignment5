import random

def randomized_quicksort(arr, min, max):
    if min < max:
        # Partitioning index
        pi = randomized_partition(arr, min, max)
        
        # Recursively sort elements before and after partition
        randomized_quicksort(arr, min, pi - 1)
        randomized_quicksort(arr, pi + 1, max)

def randomized_partition(arr, min, max):
    # Randomly select a pivot index within the given range
    pivot_index = random.randint(min, max)
    
    # Swap the randomly chosen pivot element with the last element
    arr[pivot_index], arr[max] = arr[max], arr[pivot_index]
    
    # Now proceed with the regular partitioning step
    return partition(arr, min, max)

def partition(arr, min, max):
    pivot = arr[max]  # Pivot is now at the last position after swapping
    i = min - 1  # Pointer for the smaller element
    
    for j in range(min, max):
        # If current element is smaller than or equal to the pivot, swap it
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at i+1 so that it's in its correct position
    arr[i + 1], arr[max] = arr[max], arr[i + 1]
    
    return i + 1  # Return the partitioning index

# Example usage:
arr = [-1000, -100, -10, -1, 0, 0.5, 10, 50, 99, 100, 1000]
randomized_quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
