### Majority Element
###Given an array nums of size n, return the majority element.
##The majority element is the element that appears more than ⌊n / 2⌋ times.
###You may assume that the majority element always exists in the array.
def majority(arr):
    if not arr:
        return None
    count={}
    max_element=0
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in count:
        if count[i]> len(arr)//2:
            max_element=i
    return max_element if max_element else None
### driver code
if __name__ == "__main__":
    arr = [3, 2, 3]
    print(majority(arr))  # Output: 3
    arr = [2, 2, 1, 1, 1, 2, 2]
    print(majority(arr))  # Output: 2
    arr = [1]
    print(majority(arr))  # Output: 1
    arr = []
    print(majority(arr))  # Output: None (no majority element)