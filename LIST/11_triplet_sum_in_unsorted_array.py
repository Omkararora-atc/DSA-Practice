## Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.
def find_triplet(arr,target):
    n=len(arr)
    arr.sort()
    for i in range(n-2):
        l=i+1
        r=n-1
        while l<r:
            curr=arr[i]+arr[l]+arr[r]
            if curr==target:
                return True
            elif curr<target:
                l+=1
            else:
                r-=1
    return False
### Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 9
    print("Triplet exists:", find_triplet(arr, target))
    arr = [0, -1, 2, -3, 1]
    target = 0
    print("Triplet exists:", find_triplet(arr, target))
    arr = [10, 20, 30, 40]
    target = 100
    print("Triplet exists:", find_triplet(arr, target))