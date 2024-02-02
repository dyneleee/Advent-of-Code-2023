f = open("adventinput.txt", "r")
lines = f.readlines()
total = 0

def isdigit(str):
    if str=='one':
        return 1
    if str=='two':
        return 2
    if str=='three':
        return 3
    if str=='four':
        return 4
    if str=='five':
        return 5
    if str=='six':
        return 6
    if str=='seven':
        return 7
    if str=='eight':
        return 8
    if str=='nine':
        return 9
    return -1

for i in range(0, len(lines)):
    line = lines[i]
    first = 0
    last = 0
    for j in range(0, len(line)):
        if line[j].isnumeric():
            first = int(line[j])
            break
        if j<=len(line)-3:
            sub3 = line[j:j+3]
            a3 = isdigit(sub3)
            if a3 != -1:
                first = a3
                break
        if j<=len(line)-4:
            sub4 = line[j:j+4]
            a4 = isdigit(sub4)
            if a4 != -1:
                first = a4
                break
        if j<=len(line)-5:
            sub5 = line[j:j+5]
            a5 = isdigit(sub5)
            if a5 != -1:
                first = a5
                break
    for j in range(len(line)-1, -1, -1):
        if line[j].isnumeric():
            last = int(line[j])
            break
        if j>=2:
            sub3 = line[j-2:j+1]
            a3 = isdigit(sub3)
            if a3 != -1:
                last = a3
                break
        if j>=3:
            sub4 = line[j-3:j+1]
            a4 = isdigit(sub4)
            if a4 != -1:
                last = a4
                break
        if j>=4:
            sub5 = line[j-4:j+1]
            a5 = isdigit(sub5)
            if a5 != -1:
                last = a5
                break
    calibration = 10*first+last
    total += calibration
print(total)

