f = open("CSE182db1.txt")
seqLength = 0;

for line in f:
    if line[0] == ">":
        if seqLength != 0:
            print seqLength
            #print
        print line,
        seqLength = 0;
    else:
        for char in line:
            if char.isalpha():  #is a letter
                seqLength += 1
print seqLength
    