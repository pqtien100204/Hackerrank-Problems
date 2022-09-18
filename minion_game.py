import re

def minion_game(string):
    # words with vowels & count of it == score of vowel
    vowel = "AOEUI" 
    listing = dict()
    vowel_score = 0
    conson_score = 0
    # for vow in range(len(string)):
    #     count = re.findall(string[vow], string)
    #     listing[string[vow]] = len(count)
    for vow in range(len(string)):
        for i in range(string.index(string[vow])+1, len(string)+1):
            li = [string[r:r+len(string[vow:i])] for r in range(len(string)-len(string[vow:i])+1) if string[vow:i] != '']
            result = string.count(string[vow:i])
            listing[string[vow:i]] = result

    # for elem in listing.keys():
    #     li = [string[i:i+len(elem)] for i in range(len(string)-len(elem)+1) if elem != '']
    #     result = li.count(elem)
    #     listing[elem] = result

    for element in listing.keys():
        if (element in vowel) or (element[0] in vowel):
            vowel_score += listing[element] 
        else:
            conson_score += listing[element]

    if vowel_score > conson_score:
        return f"Kevin {vowel_score}"
    elif vowel_score < conson_score:
        return f"Stuart {conson_score}"
    else:
        return "Draw"

print(minion_game("BANANA"))



# def minion_game(string):
#     vowels = 'AEIOU'

#     kevsc = 0
#     stusc = 0
#     for i in range(len(string)):
#         if s[i] in vowels:
#             kevsc += (len(string)-i)
#         else:
#             stusc += (len(string)-i)

#     if kevsc > stusc:
#         print("Kevin", kevsc)
#     elif kevsc < stusc:
#         print("Stuart", stusc)
#     else:
#         print("Draw")
        