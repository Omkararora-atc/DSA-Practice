## You are given an array arr of positive integers. Your task is to find all the leaders in the array.
# An element is considered a leader if it is greater than or equal to all elements to its right.
# The rightmost element is always a leader.
def find_lead(arr):
    res=[]
    n=len(arr)
    right=arr[-1]
    res.append(right)
    for i in range(n-2,-1,-1):
        if arr[i]>=right:
            res.append(arr[i])
            right=arr[i]
    return res[::-1]
### Driver Code
if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print("The leaders in the array are:", find_lead(arr))
    arr = [1, 2, 3, 4, 0]
    print("The leaders in the array are:", find_lead(arr))
    arr = [7, 10, 4, 10, 6, 5]
    print("The leaders in the array are:", find_lead(arr))