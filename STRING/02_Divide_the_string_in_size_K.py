### divide the string in the size of K
### if string last part is less than k then fill that with giver fill character
def divide(s,k,f):
    result=[]
    i=0
    while i<len(s):
        gr=s[i:i+k]
        if len(gr)<k:
            gr+= f*(k-len(gr))
        result.append(gr)
        i+=k
    return result
### driver code
if __name__ == "__main__":
    s = "abcdefghij"
    k = 3
    fill_char = 'x'
    result = divide(s, k, fill_char)
    print("Divided string:", result)

    # Example with a string that doesn't divide evenly
    s2 = "abcdefg"
    k2 = 3
    result2 = divide(s2, k2, fill_char)
    print("Divided string:", result2)