# Get the character count in the given string

message = "programming"

#{'p':1,'r':2,'o':1,'g':2,'a':1,'m':2,'i':1,'n':1}

char_count={}

for char in message:
    if char in char_count:
        char_count[char] = char_count[char]+1
    else:
        char_count[char]=1

print(char_count)  #{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}


