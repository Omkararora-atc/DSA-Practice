### leet code problem 167: Two Sum II - Input Array Is Sorted
def two_sum(arr,x):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]+arr[right]==x:
            return [left+1, right+1]
        elif arr[left]+arr[right]<x:
            left+=1
        else:
            right-=1
    return []
# Example usage:
if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    x = 9
    result = two_sum(arr, x)
    print(result)  # Output: [1, 2]

    arr = [2, 3, 4]
    x = 6
    result = two_sum(arr, x)
    print(result)  # Output: [1, 3]

    arr = [-1, 0]
    x = -1
    result = two_sum(arr, x)
    print(result)  # Output: [1, 2]