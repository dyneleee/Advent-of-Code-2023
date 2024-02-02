f = open("adventinput.txt", "r")
lines = f.readlines()
minimum = -1

def map(range_start, range_end, line_start, line_end):
    ranges = []
    mapped = []
    for i in range(line_start, line_end+1):
        line = lines[i].split()
        inter_start = max(range_start, int(line[1]))
        inter_end = min(range_end, int(line[1])+int(line[2])-1)
        if inter_start <= inter_end:
            mapped.append((inter_start, inter_end))
            ranges.append(inter_start+int(line[0])-int(line[1]))
            if inter_start+int(line[0])-int(line[1])==0:
                #print('0 from range '+str(range_start)+' to '+str(range_end)+' line '+str(i))
                if inter_end+int(line[0])-int(line[1])==24092690:
                    print('24092690 from range '+str(range_start)+' to '+str(range_end)+' line '+str(i))
            ranges.append(inter_end+int(line[0])-int(line[1]))
    sorted(mapped)
    current = range_start
    for i in range(0, len(mapped)):
        if current < mapped[i][0]:
            ranges.append(current)
            if current == 0:
                #print('0 from current')
                if mapped[i][0]-1==24092690:
                    print('24092690 from current')
            ranges.append(mapped[i][0]-1)
        current = mapped[i][1]+1
    if current <= range_end:
        ranges.append(current)
        ranges.append(range_end)
    return ranges

seeds = lines[0][7:len(lines[0])].split()
for i in range(0, len(seeds), 2):
    range_start = int(seeds[i])
    range_end = range_start + int(seeds[i+1]) - 1
    ranges = map(range_start, range_end, 3, 28)
    new_ranges = []
    #print(ranges)
    #print(ranges)
    for j in range(0, len(ranges), 2):
        new_ranges += map(ranges[j], ranges[j+1], 31, 49)
    ranges = new_ranges
    new_ranges = []
    #print(ranges)
    for j in range(0, len(ranges), 2):
        new_ranges += map(ranges[j], ranges[j+1], 52, 95)
    ranges = new_ranges
    new_ranges = []
    #print(ranges)
    for j in range(0, len(ranges), 2):
        new_ranges += map(ranges[j], ranges[j+1], 98, 118)
    ranges = new_ranges
    new_ranges = []
    #print(ranges)
    for j in range(0, len(ranges), 2):
        new_ranges += map(ranges[j], ranges[j+1], 121, 151)
    ranges = new_ranges
    new_ranges = []
    #print(ranges)
    for j in range(0, len(ranges), 2):
        new_ranges += map(ranges[j], ranges[j+1], 154, 202)
    ranges = new_ranges
    new_ranges = []
    #print(ranges)
    for j in range(0, len(ranges), 2):
        new_ranges += map(ranges[j], ranges[j+1], 205, 246)
    ranges = new_ranges
    new_ranges = []
    print(ranges)
    for j in range(0, len(ranges), 2):
        if (minimum == -1 or ranges[j] < minimum) and ranges[j]!=0:
            minimum = ranges[j]
    
        #soil = map(j, 3, 4)
        #fert = map(soil, 7, 9)
        #water = map(fert, 12, 15)
        #light = map(water, 18, 19)
        #temp = map(light, 22, 24)
        #hum = map(temp, 27, 28)
        #loc = map(hum, 31, 32)

        #3, 28
        #31, 49
        #52, 95
        #98, 118
        #121, 151
        #154, 202
        #205, 246
print(minimum)
