### factorial of a number using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)
### Driver Code
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = fact(n)
    print(f"The factorial of {n} is: {result}")
    print()  # For a new line after printing the result
