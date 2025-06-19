### write a selection sort algorithm in Python
def selection(arr):
    n=len(arr)
    for i in range(n-1):
        min_ind=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]
    return arr
### driver code
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    sorted_arr = selection(arr)
    print("Sorted array:", sorted_arr)