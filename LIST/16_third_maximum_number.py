### Find the third maximum number in a list.
def third_maximum(arr):
    first= second = third = float('-inf')
    for num in arr:
        if num== first or num == second or num == third:
            continue
        if num > first:
            third=second
            second=first
            first=num
        elif num > second:
            third=second
            second=num
        elif num > third:
            third=num
    return third if third != float('-inf') else first
# ### Driver code
if __name__ == "__main__":
    arr = [3, 2, 1]
    print("Original array:", arr)
    result = third_maximum(arr)
    print("Third maximum number:", result)

    arr = [1, 2]
    print("Original array:", arr)
    result = third_maximum(arr)
    print("Third maximum number:", result)

    arr = [2, 2, 3, 1]
    print("Original array:", arr)
    result = third_maximum(arr)
    print("Third maximum number:", result)
    