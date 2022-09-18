import collections
def merge_the_tools(string, k):
    # your code goes here
    len_of_substring = int(len(string) / k)
    subs = list()
    for i in range(0, len(string), int(k)):
        substr = string[i:i+k]
        subs.append(substr)
        
    result = list()
    for word in subs:
        result.append(list(item for item, count in collections.Counter(word).items()))
    
    for item in result:
        print("".join(item))