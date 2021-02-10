import re
file = input("Enter the file: ")
read = open(file)
summ = 0
for line in read:
    num = re.findall("[0-9]+", line) #list of numbers in the line
    for elem in num: #sum by adding elements inside of each line 
        elem = int(elem)
        summ = summ + elem
print(summ)

