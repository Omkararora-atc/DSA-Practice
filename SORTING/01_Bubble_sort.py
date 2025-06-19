### Write a Python program to implement bubble sort algorithm
def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
### driver code
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    sorted_arr = bubble(arr)
    print("Sorted array:", sorted_arr)
    