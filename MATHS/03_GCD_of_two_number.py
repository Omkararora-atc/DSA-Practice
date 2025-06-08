### Greatest common divisor (GCD) of two numbers
def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a % b)
# Example usage
if __name__ == "__main__":
    a = 48
    b = 18
    print(f"The GCD of {a} and {b} is: {gcd(a, b)}")  # Output: 6

    a = 56
    b = 98
    print(f"The GCD of {a} and {b} is: {gcd(a, b)}")  # Output: 14

    a = 101
    b = 10
    print(f"The GCD of {a} and {b} is: {gcd(a, b)}")  # Output: 1