f = open("adventinput.txt", "r")
lines = f.readlines()
sum = 0

for i in range(0, len(lines)):
    line = lines[i]
    #trim = line[8: len(lines)]
    sets = line.split(';')
    #possible = True
    maxb = 0
    maxg = 0
    maxr = 0
    for j in range(0, len(sets)):
        set = sets[j]
        blue = 0
        green = 0
        red = 0
        split = set.split()
        for k in range(0, len(split)):
            if split[k].isnumeric():
                if split[k+1]=='blue' or split[k+1]=='blue,':
                    blue = int(split[k])
                if split[k+1]=='green' or split[k+1]=='green,':
                    green = int(split[k])
                if split[k+1]=='red' or split[k+1]=='red,':
                    red = int(split[k])
        #if red>12 or green>13 or blue>14:
            #possible=False
        if blue>maxb:
            maxb=blue
        if red>maxr:
            maxr=red
        if green>maxg:
            maxg=green
    #if possible:
        #sum += i+1
    power = maxb*maxr*maxg
    sum += power
print(sum)