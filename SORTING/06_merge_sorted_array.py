###Given two arrays arr1 and arr2 of size m and n respectively, merge them in sorted order into a single array arr1 of size m+n.
def merge(arr1,arr2,m,n):
    temp=arr1[:m]
    i,j,k=0,0,0
    while i<m and j<n:
        if temp[i]>=arr2[j]:
            arr1[k]=arr2[j]
            j+=1
        else:
            arr1[k]=temp[i]
            i+=1
        k+=1
    while i<m:
        arr1[k]=temp[i]
        i+=1
        k+=1
    while j<n:
        arr1[k]=arr2[j]
        j+=1
        k+=1
# Example usage
if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 0, 0, 0]
    arr2 = [2, 4, 6]
    m = 4
    n = 3
    merge(arr1, arr2, m, n)
    print("Merged array:", arr1)  # Output: Merged array: [1, 2, 3, 4, 5, 6, 7]