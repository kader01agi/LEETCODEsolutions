def isSubstringPresent(s: str) -> bool:
    sReversed = s[::-1]
    susString = [s[i:i+2] for i in range(len(s) - 1)]
    for i in susString:
        return i in sReversed
print(isSubstringPresent('abcd'))