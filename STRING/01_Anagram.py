### Given two strings s1 and s2 consisting of lowercase characters.
# The task is to check whether two given strings are an anagram of each other or not.
def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    for i in count:
        if i!=0:
            return False
    return True
# Example usage
s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))  # Output: True
s1 = "hello"
s2 = "world"
print(is_anagram(s1, s2))  # Output: False


