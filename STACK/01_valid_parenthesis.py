### Write a code to check if a string has valid parentheses
def is_balanced(s):
    stack=[]
    for x in s:
        if x in('(','{','['):
            stack.append(x)
        else:
            if  not stack:
                return False
            elif is_matching(stack[-1],x)==False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True
def is_matching(a,b):
    if (a=='(' and b==")") or (a=='{' and b=='}') or (a=='[' and b==']'):
        return True
    return False
# ### Driver code
if __name__ == "__main__":
    test_strings = [
        "()",
        "({[]})",
        "({[}])",
        "((()))",
        "((())",
        "([{}])",
        "{[()]}",
        "{[(])}"
    ]

    for s in test_strings:
        print(f"{s}: {'Balanced' if is_balanced(s) else 'Not Balanced'}")



