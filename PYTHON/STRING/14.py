def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix =""
    strs.sort()
    for i in range(min(len(strs[0]), len(strs[-1]))):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]
        else:
            break

    return prefix        


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))





