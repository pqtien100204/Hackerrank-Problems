import string
alphabet = list(string.ascii_lowercase)
def print_rangoli(size):
    # your code goes here
    set_of_words = list(alphabet[:size])
    
    # dash_line = (((int(size) * 2) - 1) + ((int(size) * 2) - 2))
    # frame = ("-" * (((int(size) * 2) - 1) + ((int(size) * 2) - 2)))
    
    # up_string = [set_of_words[size-i].center(dash_line, "-") for i in range(1, size+1)]
    # down_string = [set_of_words[i].center(dash_line, "-") for i in range(1, size)]
    
        
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = set_of_words[size:x:-1]+set_of_words[x:size]
        print ("--"*x+ '-'.join(line) +"--"*x)
    
    
    