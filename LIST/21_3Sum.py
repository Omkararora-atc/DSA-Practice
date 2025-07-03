#### find all the triplets in the array that sum to zero
def three(arr):
    arr.sort()
    res=[]
    for i in range(len(arr)-2):
        if i>0 and arr[i]== arr[i-1]:
            continue
        l, r = i + 1, len(arr) - 1
        while l<r:
            total=arr[l]+arr[r]+arr[i]
            if total == 0:
                res.append([arr[i],arr[l],arr[r]])
                l+=1
                r-=1
                while l<r and arr[l] == arr[l-1]:
                    l+=1
                while l<r and arr[r] == arr[r+1]:
                    r-=1
            elif total < 0:
                l+=1
            else:
                r-=1
    return res
#### driver code
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(three(arr))  # Output: [[-1, -1, 2], [-1, 0, 1]]
    arr = [0, 0, 0]
    print(three(arr))  # Output: [[0, 0, 0]]
    arr = [1, 2, -2, -1]
    print(three(arr))  # Output: []