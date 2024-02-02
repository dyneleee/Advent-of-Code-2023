f = open("adventinput.txt", "r")
lines = f.readlines()
sum = 0

def getnum(line_ind, num_ind):
    str = lines[line_ind][num_ind]
    if num_ind > 0:
        if lines[line_ind][num_ind-1].isnumeric():
            str = lines[line_ind][num_ind-1] + str
            if num_ind > 1:
                if lines[line_ind][num_ind-2].isnumeric():
                    str = lines[line_ind][num_ind-2] + str
    if num_ind + 1 < len(lines[line_ind]):
        if lines[line_ind][num_ind+1].isnumeric():
            str += lines[line_ind][num_ind+1]
            if num_ind + 2 < len(lines[line_ind]):
                if lines[line_ind][num_ind+2].isnumeric():
                    str += lines[line_ind][num_ind+2]
    return int(str)

def prodiftwo(line_ind, star_ind):
    nums = []
    # no stars in first or last rows/cols
    char1 = lines[line_ind-1][star_ind-1]
    char2 = lines[line_ind-1][star_ind]
    char3 = lines[line_ind-1][star_ind+1]
    if char2.isnumeric():
        nums.append(getnum(line_ind-1, star_ind))
    elif char1.isnumeric() and char3.isnumeric():
        nums.append(getnum(line_ind-1, star_ind-1))
        nums.append(getnum(line_ind-1, star_ind+1))
    elif char1.isnumeric():
         nums.append(getnum(line_ind-1, star_ind-1))
    elif char3.isnumeric():
        nums.append(getnum(line_ind-1, star_ind+1))

    if lines[line_ind][star_ind-1].isnumeric():
        nums.append(getnum(line_ind, star_ind-1))
    if lines[line_ind][star_ind+1].isnumeric():
        nums.append(getnum(line_ind, star_ind+1))

    char1 = lines[line_ind+1][star_ind-1]
    char2 = lines[line_ind+1][star_ind]
    char3 = lines[line_ind+1][star_ind+1]
    if char2.isnumeric():
        nums.append(getnum(line_ind+1, star_ind))
    elif char1.isnumeric() and char3.isnumeric():
        nums.append(getnum(line_ind+1, star_ind-1))
        nums.append(getnum(line_ind+1, star_ind+1))
    elif char1.isnumeric():
         nums.append(getnum(line_ind+1, star_ind-1))
    elif char3.isnumeric():
        nums.append(getnum(line_ind+1, star_ind+1))

    if len(nums) == 2:
        return nums[0]*nums[1]
    return 0

for i in range(0, len(lines)):
    line = lines[i]
    #print(line)
    for j in range(0, len(line)):
        if line[j]=='*':
            #print('*')
            prod = prodiftwo(i, j)
            if prod != 0:
                #print(prod)
                sum += prod
print(sum)