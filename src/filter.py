infile = open("CSE182db1.txt")
outfile = open("filteroutput.txt", 'w')

LINE_LENGTH = 60
writing = False
count = 0
ignoreFirst = False

for line in infile:
    if line[0] == ">":
        count = 0
        if 'Mus musculus' or 'RAT' or 'Rattus norvegicus' in line:
            writing = True
            if ignoreFirst:
                outfile.write('\n')
            ignoreFirst = True
            outfile.write(line)
        else:
            writing = False
    elif writing:
        for char in line:
            if char.isalpha():  #is a letter
                outfile.write(char)
                count += 1
                if count == LINE_LENGTH:
                    outfile.write('\n')
                    count -= LINE_LENGTH
        

    