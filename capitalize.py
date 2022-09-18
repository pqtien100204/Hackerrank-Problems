import re
import string

words =  string.ascii_lowercase
def solve(s):
    componn = s.split(" ")
    print(componn)
    tokens = re.findall('\s+', s)
    new_name = [i.capitalize() for i in componn]
    print(" ".join(new_name))
            
print(solve("helooo    hahaha  n"))