## write the code to find all unique quadruplets in an array that sum to a target value
def four(arr):
    arr.sort()
    res=[]
    for i in range(len(arr)-3):
        if i>0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, len(arr)-2):
            if j>i+1 and arr[j] == arr[j+1]:
                continue
            left,right= j+1, len(arr)-1
            while left<right:
                total= arr[i] + arr[j] + arr[left] + arr[right]
                if total ==0:
                    res.append([arr[i], arr[j], arr[left], arr[right]])
                    left+=1
                    right-=1
                    while left<right and arr[left] == arr[left-1]:
                        left+=1
                    while left<right and arr[right] == arr[right+1]:
                        right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
    return res
### driver code
if __name__ == "__main__":
    arr = [1, 0, -1, 0, -2, 2]
    print(four(arr))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    arr = [0, 0, 0, 0]
    print(four(arr))  # Output: [[0, 0, 0, 0]]
    arr = [1, 2, -2, -1]
    print(four(arr))  # Output: []