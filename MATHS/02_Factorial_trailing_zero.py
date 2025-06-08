### factorial trailing zeroes
def trailing(n):
    count=0
    i=5
    while n//i>0:
        count+=n//i
        i*=5
    return count
# Example usage
if __name__ == "__main__":
    n = 100
    print(f"The number of trailing zeroes in {n}! is: {trailing(n)}")  # Output: 24
    n = 25
    print(f"The number of trailing zeroes in {n}! is: {trailing(n)}")  # Output: 6
    n = 50
    print(f"The number of trailing zeroes in {n}! is: {trailing(n)}")  # Output: 12