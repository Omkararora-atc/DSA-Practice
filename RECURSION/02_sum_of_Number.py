### You are given a number n. You need to find the sum of digits of n.
def sum(n):
    if n==0:
        return 0
    return n%10+sum(n//10)
### Driver Code
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = sum(n)
    print(f"The sum of digits of {n} is: {result}")
    print()  # For a new line after printing the result
