# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip() #strips whitespace from right side of a string
#     if line.startswith('From:'):
#         print(line)

# or

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() #strips whitespace from right side of a string
    if line.startswith('From:'):
        continue
    print(line)
