### fibonacci series using recursion
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
### Driver Code
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = fib(n)
    print(f"The {n}th Fibonacci number is: {result}")
    print()  # For a new line after printing the result