### Subarray with given sum
def sub_array(arr,target):
    s,curr=0,0
    n=len(arr)
    for i in range(n):
        curr+=arr[i]
        while curr>target and s<i:
            curr-=arr[s]
            s+=1
        if curr==target:
            return True
    return False
### Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    target = 16
    print(sub_array(arr, target))
    arr = [1, 2, 3, 4, 5]
    target = 50
    print(sub_array(arr, target))
    arr = [1, 2, 3, 4, 5]
    target = 10
    print(sub_array(arr, target))