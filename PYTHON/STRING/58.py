def lengthOfLastWord(s: str) -> int:
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    A word is a maximal substring  consisting of non-space characters only.
    """ 
    s = s.strip()
    strList = s.split(" ")
    print(strList)
    return len(strList[-1])

s = "Hello World"
s1 = "   fly me   to   the moon  "
print(lengthOfLastWord(s1))
