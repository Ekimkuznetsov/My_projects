name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith("From"): continue
    nl = line.split()
    if not len(nl[0]) == 4: continue
    autor = nl[1]
    counts[autor] = counts.get(autor, 0) +1
bigcount = None
bigautor = None
for autor,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigautor = autor
print(bigautor, bigcount)
