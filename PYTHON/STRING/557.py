def reverseWords(s: str) -> str:
    """Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order."""
    sList = s.strip().split(" ")
    reversedChar = [i[::-1] for i in sList]
    return " ".join(reversedChar)

print(reverseWords("Let's take LeetCode contest"))