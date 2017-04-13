infile = open("CSE182db1.txt")
outfile = open("data.in", 'w')

PRINTING_TERMINATION = 2
offset = 0
printing = 0

for line in infile:
    if line[0] == '>':
        for char in line:
            if char == '|':
                printing += 1
                if printing == PRINTING_TERMINATION:
                    printing = 0
                    break
            elif printing == 1:
                outfile.write(char)
    
        outfile.write(' ')
        outfile.write(str(offset))
        outfile.write('\n')
    else:
        for char in line:
            if char.isalpha():
                offset += 1