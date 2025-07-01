### maximum average subarray I
## leet code 643
def maximum_avg(arr,k):
    n=len(arr)
    if n<k:
        return 0
    curr= sum(arr[:k])
    res=curr
    for i in range(k,n):
        curr=curr+arr[i]-arr[i-k]
        res=max(res,curr)
    return res/k
# ### Driver code
if __name__ == "__main__":
    arr = [1, 12, -5, -6, 50, 3]
    k = 4
    print("Original array:", arr)
    result = maximum_avg(arr, k)
    print("Maximum average of subarray of size", k, ":", result)

    arr = [5, 5, 5, 5]
    k = 2
    print("Original array:", arr)
    result = maximum_avg(arr, k)
    print("Maximum average of subarray of size", k, ":", result)