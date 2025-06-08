### Print 1to n Numbers without using loop
def print_num(n):
    if n==0:
        return
    print_num(n-1)
    print(n,end=" ")
### Driver  Code
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_num(n)
    print()  # For a new line after printing all numbers
