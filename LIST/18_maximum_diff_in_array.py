### Maximum difference in array
def maxi_diff(arr):
    n=len(arr)
    mini_val=arr[0]
    max_diff=arr[1]-arr[0]
    for i in range(1,n):
        max_diff=max(max_diff,arr[i]-mini_val)
        mini_val=min(mini_val,arr[i])
    return max_diff
# ### Driver code
if __name__ == "__main__":
    arr = [2, 3, 10, 6, 4, 8, 1]
    print("Original array:", arr)
    result = maxi_diff(arr)
    print("Maximum difference in array:", result)

    arr = [7, 9, 5, 6, 3, 2]
    print("Original array:", arr)
    result = maxi_diff(arr)
    print("Maximum difference in array:", result)

    arr = [1, 2]
    print("Original array:", arr)
    result = maxi_diff(arr)
    print("Maximum difference in array:", result)