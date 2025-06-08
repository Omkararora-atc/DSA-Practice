### Palindrome or not
class Solution(object):
    def is_palindrome(self,x):
        if x<0:
            return False
        if x==0:
            return True
        y=0
        while x>0:
            a=x%10
            y=y*10+a
            x=x//10
        return y==x

# Example usage
if __name__ == "__main__":
    sol = Solution()
    number = 121
    if sol.is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

    number = -121
    if sol.is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

    number = 10
    if sol.is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")