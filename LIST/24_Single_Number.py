def single_number(arr):
    count={}
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in count:
        if count[i]==1:
            return i
    return -1
### driver code
if __name__ == "__main__":
    arr = [4, 1, 2, 1, 2]
    print(single_number(arr))  # Output: 4
    arr = [2, 2, 1]
    print(single_number(arr))  # Output: 1
    arr = [1]
    print(single_number(arr))  # Output: 1
    arr = []
    print(single_number(arr))  # Output: -1