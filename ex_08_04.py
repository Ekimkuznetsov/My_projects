fname = input("Enter file name: ")
fh = open(fname)
fst = list()
for line in fh:
    x = line.split()
    for word in x:
        if word not in fst:
            fst.append(word)  
fst.sort()
print(fst)





