### Given an array arr of integers, find all the elements that occur more than once in the array.
# If no element repeats, return an empty array.
def duplicates(arr):
    res=[]
    count={}
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for key, value in count.items():
        if value > 1:
            res.append(key)
    return res
# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 1, 2]
    print(f"Duplicate elements in {arr}: {duplicates(arr)}")  # Output: [1, 2]

    arr = [5, 4, 3, 2, 1]
    print(f"Duplicate elements in {arr}: {duplicates(arr)}")  # Output: []

    arr = []
    print(f"Duplicate elements in {arr}: {duplicates(arr)}")  # Output: []

    arr = [1]
    print(f"Duplicate elements in {arr}: {duplicates(arr)}")  # Output: []