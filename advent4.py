f = open("adventinput.txt", "r")
lines = f.readlines()
sum = 0
copies = []
for i in range(0, len(lines)):
    copies.append(1)

for i in range(0, len(lines)):
    winning = lines[i][lines[i].index(':')+2:lines[i].index('|')].split()
    yours = lines[i][lines[i].index('|')+2:len(lines[i])].split()
    count = 0
    for num in yours:
        if num in winning:
            count += 1
    for j in range(i+1, i+count+1):
        copies[j] += copies[i]
for i in range(0, len(lines)):
    sum += copies[i]
print(sum)