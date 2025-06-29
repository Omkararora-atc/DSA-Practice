def count_prime(n):
    if n<2:
        return 0
    prime=[True]*n
    prime[0]=prime[1]=False
    p=2
    while p*p<n:
        if prime[p]:
            for i in range(p*p,n,p):
                prime[i]=False
        p+=1
    return sum(prime)
# Example usage
if __name__ == "__main__":
    n = 10
    result = count_prime(n)
    print(f"Number of prime numbers less than {n}: {result}")  # Output: Number of prime numbers less than 10: 4

    n = 20
    result = count_prime(n)
    print(f"Number of prime numbers less than {n}: {result}")  # Output: Number of prime numbers less than 20: 8

    n = 1
    result = count_prime(n)
    print(f"Number of prime numbers less than {n}: {result}")  # Output: Number of prime numbers less than 1: 0
