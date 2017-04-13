infile = open("CSE182db1.txt")
outfile = open("data.seq", 'w')

ignoreFirst = True

for line in infile:
    if ignoreFirst:
        ignoreFirst = False
        continue
    if line[0] == '>':
        outfile.write('@')
    else:
        for char in line:
            if char.isalpha():  #is a letter
                outfile.write(char)