# Quick Sort
array_quick = [2,4,6,7,5,4,1,2,3,99,77,66,55,75]

def partition_array(arr, low, high):
    pivot = array_quick[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quicksort(arr, low=0, high = None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition_array(arr, low, high)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index+1, high)

quicksort(array_quick)
print('QUICK SORT', array_quick)


# Merge Sort
array_merge = [2,4,6,7,5,4,1,2,3,99,77,66,55,75]

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result
 

print('Sorted array', mergeSort(array_merge))
