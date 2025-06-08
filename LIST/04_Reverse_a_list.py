### Reverse a list in Python
def reverse_list(arr):
    n=len(arr)
    left,right=0,n-1
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
## Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reversed_arr = reverse_list(arr)
    print(f"Reversed list: {reversed_arr}")

    arr = [5, 4, 3, 2, 1]
    reversed_arr = reverse_list(arr)
    print(f"Reversed list: {reversed_arr}")

    arr = []
    reversed_arr = reverse_list(arr)
    print(f"Reversed list: {reversed_arr}")

    arr = [1]
    reversed_arr = reverse_list(arr)
    print(f"Reversed list: {reversed_arr}")