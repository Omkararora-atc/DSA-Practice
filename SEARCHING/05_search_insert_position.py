def search(arr,x):
    left,right = 0,len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left
# Example usage
if __name__ == "__main__":
    arr = [1, 3, 5, 6]
    x = 5
    result = search(arr, x)
    print(f"Insert position for {x} in {arr}: {result}")  # Output: 2

    arr = [1, 3, 5, 6]
    x = 2
    result = search(arr, x)
    print(f"Insert position for {x} in {arr}: {result}")  # Output: 1

    arr = [1, 3, 5, 6]
    x = 7
    result = search(arr, x)
    print(f"Insert position for {x} in {arr}: {result}")  # Output: 4

    arr = [1, 3, 5, 6]
    x = 0
    result = search(arr, x)
    print(f"Insert position for {x} in {arr}: {result}")  # Output: 0