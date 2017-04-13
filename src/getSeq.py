sequence = open("data.seq")
locater = open("data.in")

query = raw_input("Please enter your query: ")

file_contents = sequence.read()

index = file_contents.find(query)

if index != -1:
    for line in reversed(locater.readlines()):
        start = line.find(" ")
        value = int(line[start+1:])
        if index > value:
            #Printing as a form of returning the gi number
            print line[:start]
            break
else:
    print "The query is not present."