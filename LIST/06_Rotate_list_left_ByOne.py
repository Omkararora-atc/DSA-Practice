### Rotate the list left by one position
def left(arr,n):
    if not arr or n<=0:
        return arr
    i=arr[0]
    for j in range(1,n):
        arr[j-1]=arr[j]
    arr[n-1]=i
    return arr
## Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    rotated_arr = left(arr, n)
    print(f"List after rotating left by one: {rotated_arr}")

    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    rotated_arr = left(arr, n)
    print(f"List after rotating left by one: {rotated_arr}")

    arr = []
    n = len(arr)
    rotated_arr = left(arr, n)
    print(f"List after rotating left by one: {rotated_arr}")

    arr = [1]
    n = len(arr)
    rotated_arr = left(arr, n)
    print(f"List after rotating left by one: {rotated_arr}")