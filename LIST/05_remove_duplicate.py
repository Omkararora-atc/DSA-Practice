#### Remove the duplicates from a list
def remove_duplicates(arr):
    if not arr:
        return None
    i=1
    for j in range(1,len(arr)):
        if arr[j]!=arr[i-1]:
            arr[i]=arr[j]
            i+=1
    return arr[:i]
## Driver code
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 5]
    unique_arr = remove_duplicates(arr)
    print(f"Array after removing duplicates: {unique_arr}")

    arr = [5, 4,9,9,9,9, 3, 2, 1]
    unique_arr = remove_duplicates(arr)
    print(f"Array after removing duplicates: {unique_arr}")

    arr = []
    unique_arr = remove_duplicates(arr)
    print(f"Array after removing duplicates: {unique_arr}")

    arr = [1]
    unique_arr = remove_duplicates(arr)
    print(f"Array after removing duplicates: {unique_arr}")
