#### Move all the zeros to the right side of the array while maintaining the order of non-zero elements.
def move_zeros(arr):
    n=len(arr)
    j=0
    for i in range(n):
        if arr[i]!=0:
            arr[i],arr[j] = arr[j], arr[i]
            j+=1
    return arr
### Driver code
if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    print("Original array:", arr)
    result = move_zeros(arr)
    print("Array after moving zeros:", result)
