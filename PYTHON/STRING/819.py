# 819 Most Common Word
""" Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase."""


# def mostCommonWord(paragraph: str, banned: list[str]) -> str:
#     paragraph = paragraph.lower().split()
#     sieved = [word for word in paragraph if word not in banned]
#     sieved = [word.strip(".,!?;:") for word in sieved]
#     print(sieved)
#     max_count = 0
#     max_element = None
#     for element in sieved:
#         count = sieved.count(element)
#         if count > max_count:
#             max_count = count
#             max_element = element
#     return max_element


# # scenario 1
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# # scenario 2
# # paragraph = "a."
# # banned = []
# print(mostCommonWord(paragraph, banned))



from collections import defaultdict


def mostCommonWord( paragraph: str, banned: list[str]) -> str:
    # first we need to remove the symbols that can be present, and replacing with space
    symbols = "!?',;."
    for i in symbols:
        paragraph = paragraph.replace(i, " ")
    hashMap = defaultdict(int)
    # converting to lower case
    paragraph = paragraph.lower()
    # splitting based on space to put the given words to a list
    list1 = paragraph.split()

    # checking if the word not in banned , and incrementing its count
    for i in list1:
        if i not in banned:
            hashMap[i] = hashMap[i] + 1

    # finding the word has occurs most number of times
    maximum = max(hashMap.values())

    # finding the value of key for the word with maximum count
    for key, value in hashMap.items():
        if value == maximum:
            return key

# # scenario 1
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# # scenario 2
# # paragraph = "a."
# # banned = []
print(mostCommonWord(paragraph, banned))