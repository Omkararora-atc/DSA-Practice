### Implementation of Quick Sort using Hoare's partitioning scheme
def hoare(arr,l,h):
    pivot = arr[l]
    i = l - 1
    j = h + 1
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
def quick_sort(arr, l, h):
    if l < h:
        p = hoare(arr, l, h)
        quick_sort(arr, l, p)
        quick_sort(arr, p + 1, h)
### driver code
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
