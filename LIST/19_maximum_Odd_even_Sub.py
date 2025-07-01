### maximum odd even subarray count
def count_odd_even(arr):
    maxx_count=1
    curr=1
    n=len(arr)
    for i in range(n):
        if (arr[i-1]%2==0 and arr[i]%2!=0) or (arr[i-1]%2!=0 and arr[i]%2==0):
            curr+=1
            maxx_count=max(maxx_count, curr)
        else:
            curr=1
    return maxx_count
## driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    result = count_odd_even(arr)
    print("Maximum odd-even subarray count:", result)

    arr = [2, 3, 4, 5, 6]
    print("Original array:", arr)
    result = count_odd_even(arr)
    print("Maximum odd-even subarray count:", result)

    arr = [1, 3, 5, 7]
    print("Original array:", arr)
    result = count_odd_even(arr)
    print("Maximum odd-even subarray count:", result)