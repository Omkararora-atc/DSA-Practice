def two_sum(arr,target):
    left,right=0,len(arr)-1
    while left<right:
        curr=arr[left]+arr[right]
        if curr==target:
            return [left+1,right+1]
        elif curr<target:
            left+=1
        else:
            right-=1
    return []
### Driver code
if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9
    result = two_sum(arr, target)
    print(f"Indices of numbers that add up to {target}: {result}")  # Output: [1, 2]

    arr = [1, 2, 3, 4, 6]
    target = 10
    result = two_sum(arr, target)
    print(f"Indices of numbers that add up to {target}: {result}")  # Output: [4, 5]

    arr = [1, 2]
    target = 3
    result = two_sum(arr, target)
    print(f"Indices of numbers that add up to {target}: {result}")  # Output: [1, 2]

