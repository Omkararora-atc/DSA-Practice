### print all prime numbers in a given range
def isprime(n):
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
def toprime(n):
    prime=[]
    for i in range(n):
        if isprime(i):
            prime.append(i)
    return  prime
# Example usage
if __name__ == "__main__":
    n = 50
    primes = toprime(n)
    print(f"Prime numbers up to {n}: {primes}")  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    n = 100
    primes = toprime(n)
    print