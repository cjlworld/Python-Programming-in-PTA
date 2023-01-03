str = ""
letter, blank, digit, other = 0, 0, 0, 0
while len(str) + blank <= 10 :
    s = input()
    str = str + s
    blank = blank + 1
blank = blank - 1
for c in str :
    if c.isalpha() : 
        letter = letter + 1
    elif c.isspace() :
        blank = blank + 1
    elif c.isdigit() :
        digit = digit + 1 
    else :
        other = other + 1

print("letter = {:d}, blank = {:d}, digit = {:d}, other = {:d}".format(letter, blank, digit, other))

