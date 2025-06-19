### implementation of quick sort using lomuto partition scheme
def lomuto(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1
def quick_sort(arr,l,h):
   if l<h:
       p=lomuto(arr,l,h)
       quick_sort(arr,l,p-1)
       quick_sort(arr,p+1,h)
### driver code
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
    
