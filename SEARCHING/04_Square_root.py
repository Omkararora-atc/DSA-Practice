### Find the square root of a number using binary search
def square_root(n):
    if n==0 or n==1:
        return n
    left, right = 0, n
    ans=0
    while left<=right:
        mid=(left + right) // 2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            left = mid + 1
            ans=mid
        else:
            right = mid - 1
    return ans
### Driver code
if __name__ == "__main__":
    n = 16
    result = square_root(n)
    print(f"The square root of {n} is approximately {result}")
    n = 20
    result = square_root(n)
    print(f"The square root of {n} is approximately {result}")
