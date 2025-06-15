### Given an integer array arr[] and a number k.
# Find the count of distinct elements in every window of size k in the array.
def count_dis(arr,k):
    count={}
    res=[]
    n=len(arr)
    for i in range(k):
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1
    res.append(len(count))
    for i in range(k,n):
        count[arr[i-k]]-=1
        if count[arr[i-k]] == 0:
            del count[arr[i-k]]
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1
        res.append(len(count))
    return  res
### Driver code
if __name__ == "__main__":
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    print(count_dis(arr, k))  # Output: [3, 4,4, 3]
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 3
    print(count_dis(arr, k))  # Output: [2, 3, 3, 3,3]
