from itertools import count


f1 = open("1.txt","r")
count = 0
for line in f1 :
    count = count + 1
print("Line count: ",count)