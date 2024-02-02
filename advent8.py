import math
f = open("adventinput.txt", "r")
lines = f.readlines()
directions = 'LRLRRLLRRLRRRLRLRRRLLRRLLLLRRRLRRRLRRLRRLRRRLRRRLLRRLRLRRLRRRLLLRRLRRLLRLLRRRLRRRLLRLRRRLRLLRRLLLRLRRRLRRRLRRRLLRLRRRLLRRLRLRLLRRLRRRLRRLRLLRLRRRLRRLRLRLRRLRRRLRRRLRRRLRRLRRRLLRRLRRLLRRRLLRLRLRLRLLLRRLRLRRLRRLRRLRRLRRRLRRRLRLRRRLRLRRRLRRLRLLRLRRLRLRLLLRLLLRRRLRRLLLRLRRRR'
#LRLRRLLRRLRRRLRLRRRLLRRLLLLRRRLRRRLRRLRRLRRRLRRRLLRRLRLRRLRRRLLLRRLRRLLRLLRRRLRRRLLRLRRRLRLLRRLLLRLRRRLRRRLRRRLLRLRRRLLRRLRLRLLRRLRRRLRRLRLLRLRRRLRRLRLRLRRLRRRLRRRLRRRLRRLRRRLLRRLRRLLRRRLLRLRLRLRLLLRRLRLRRLRRLRRLRRLRRRLRRRLRLRRRLRLRRRLRRLRLLRLRRLRLRLLLRLLLRRRLRRLLLRLRRRR
dict = {}
current = []
start = []
loops = [0, 0, 0, 0, 0, 0]
count = 0
print(math.lcm(18157, 14363, 19783, 15989, 19241, 12737))

for i in range(0, len(lines)):
    key = lines[i][0:3]
    if key[2] == 'A':
        current.append(key)
        start.append(key)
    left = lines[i][7:10]
    right = lines[i][12:15]
    dict[key] = left+right

print(current)
end = False
check_end = True
for i in range(0, len(current)):
    if current[i][2] != 'Z':
        check_end = False
end = check_end
while not end:
    #print(current)
    dir = directions[count % len(directions)]
    count += 1
    if dir == 'L':
        for i in range(0, len(current)):
            current[i] = dict[current[i]][0:3]
    else:
        for i in range(0, len(current)):
            current[i] = dict[current[i]][3:6]
    if current[2][2] == 'Z':
        print(str(count))
        #print(str(i)+ ' '+str(count))
    #print(dir+' '+current)
    check_end = True
    for i in range(0, len(current)):
        if current[i][2] != 'Z':
            check_end = False
    end = check_end

print(count)

