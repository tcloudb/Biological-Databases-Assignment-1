f = open("CSE182db1.txt")
sm = 0;

for line in f:
    if line[0] != '>':
        for char in line:
            if char.isalpha():
                sm += 1;
        print sm
        