def count_substring(string, sub_string):
    li = [string[i:i+len(sub_string)] for i in range(len(string)-len(sub_string)+1)]
    result = li.count(sub_string)
    return result

print(count_substring("ABCDCDC", "CDC"))