### Given an array arr[].
# Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer.
# Do the mentioned change in the array in place
def rotate(arr,d):
    if not arr:
        return []
    n=len(arr)
    d=d%n
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
## Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = 2
    rotate(arr, d)
    print(f"Array after rotating left by {d} steps: {arr}")

    arr = [5, 4, 3, 2, 1]
    d = 3
    rotate(arr, d)
    print(f"Array after rotating left by {d} steps: {arr}")

    arr = []
    d = 1
    rotate(arr, d)
    print(f"Array after rotating left by {d} steps: {arr}")

    arr = [1]
    d = 0
    rotate(arr, d)
    print(f"Array after rotating left by {d} steps: {arr}")