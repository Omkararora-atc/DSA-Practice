### Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
def reverse(x):
    if x < 0:
        sign=-1
    else:
        sign=1
    x = abs(x)
    reversed_x = 0
    while x>0:
        digit = x % 10
        x //= 10
        reversed_x = reversed_x * 10 + digit
    reversed_x *= sign
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x
# Example usage
if __name__ == "__main__":
    print(reverse(123))        # Output: 321
    print(reverse(-123))       # Output: -321
    print(reverse(120))        # Output: 21
    print(reverse(0))          # Output: 0
    print(reverse(1534236469)) # Output: 0 (out of range)
    print(reverse(-2147483648)) # Output: 0 (out of range)