import sys
sys.setrecursionlimit(6000)

f = open("adventinput.txt", "r")
out = open("adventoutput.txt", "w")
out2 = open("output.txt", "w")
lines = f.readlines()
path = []
dists = []
max = -1

def check(row, col):
    if row < 0 or row >= len(path):
        return False
    if col < 0 or col >= len(path[0]):
        return False
    return True

def unfilled(row, col):
    if path[row][col] != '*' and path[row][col] != 'O':
        return True
    return False

def fill(row, col):
    path[row][col] = 'O'
    if check(row-1, col):
        if unfilled(row-1, col):
            fill(row-1, col)
    if check(row+1, col):
        if unfilled(row+1, col):
            fill(row+1, col)
    if check(row, col-1):
        if unfilled(row, col-1):
            fill(row, col-1)
    if check(row, col+1):
        if unfilled(row, col+1):
            fill(row, col+1)

count = 1
pr_r = 0
pr_c = 0
row = 0
col = 0
for i in range(0, len(lines)):
    path.append([])
    for j in range(0, len(lines[i])):
        if lines[i][j] != '\n':
            path[i].append(lines[i][j])
        if lines[i][j] == 'S':
            row = i
            col = j

while True:
    #print(str(row)+' '+str(col))
    out2.write(lines[row][col]+'\n')
    path[row][col]='*'
    if lines[row][col] == 'S':
        if count > 1:
            break
        if check(row, col+1):
            if lines[row][col+1] == '-' or lines[row][col+1] == 'J' or lines[row][col+1] == '7':
                pr_r = row
                pr_c = col
                col += 1
                continue
        if check(row, col-1):
            if lines[row][col+1] == '-' or lines[row][col+1] == 'L' or lines[row][col+1] == 'F':
                pr_r = row
                pr_c = col
                col -= 1
                continue
        if check(row-1, col):
            if lines[row-1][col] == '|' or lines[row-1][col] == '7' or lines[row-1][col] == 'F':
                pr_r = row
                pr_c = col
                row -= 1
                continue
        if check(row+1, col):
            if lines[row+1][col] == '|' or lines[row+1][col] == 'L' or lines[row+1][col] == 'J':
                pr_r = row
                pr_c = col
                row += 1
                continue
    count += 1
    if lines[row][col] == '|':
        if pr_r == row-1:
            pr_r = row
            pr_c = col
            row += 1
            continue
        pr_r = row
        pr_c = col
        row -= 1
        continue
    if lines[row][col] == '-':
        if pr_c == col-1:
            pr_r = row
            pr_c = col
            col += 1
            continue
        pr_r = row
        pr_c = col
        col -= 1
        continue
    if lines[row][col] == 'L':
        if pr_r == row-1:
            pr_r = row
            pr_c = col
            col += 1
            continue
        pr_r = row
        pr_c = col
        row -= 1
        continue
    if lines[row][col] == 'J':
        if pr_r == row-1:
            pr_r = row
            pr_c = col
            col -= 1
            continue
        pr_r = row
        pr_c = col
        row -= 1
        continue
    if lines[row][col] == '7':
        if pr_r == row+1:
            pr_r = row
            pr_c = col
            col -= 1
            continue
        pr_r = row
        pr_c = col
        row += 1
        continue
    if lines[row][col] == 'F':
        if pr_r == row+1:
            pr_r = row
            pr_c = col
            col += 1
            continue
        pr_r = row
        pr_c = col
        row += 1
        continue
#for i in range(len(lines)):
    #for j in range(len(path[i])):
        #if path[i][j] == '*':
            #out.write(lines[i][j])
        #else:
            #out.write('$')
    #out.write('\n')
print(count)

path_count = 0
for i in range(len(path)):
    if path[i][0] != '*':
        fill(i, 0)
    if path[i][len(path[i])-1] != '*':
        fill(i, len(path[i])-1)
for i in range(len(path[0])):
    if path[0][i] != '*':
        fill(0, i)
    if path[len(path)-1][i] != '*':
        fill(len(path)-1, i)
#fill(0, 0)
for i in range(len(path)):
    for j in range(len(path[i])):
        if path[i][j] == '*':
            path_count += 1
        out.write(path[i][j])
    out.write('\n')
print(path_count)
interior = 0
for i in range(len(path)):
    for j in range(len(path[i])):
        if unfilled(i, j):
            interior += 1
print(interior)

