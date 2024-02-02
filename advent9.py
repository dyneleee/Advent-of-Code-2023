f = open("adventinput.txt", "r")
lines = f.readlines()
sum = 0

def find_next(arr):
    zeros = True
    for num in arr:
        if num != 0:
            zeros = False
            break
    if zeros:
        return 0
    diffs = []
    for i in range(0, len(arr)-1):
        diffs.append(arr[i+1]-arr[i])
    return arr[len(arr)-1] + find_next(diffs)

for line in lines:
    split = line.split()
    arr = []
    for i in range(len(split)-1, -1, -1):
        arr.append(int(split[i]))
    sum += find_next(arr)
print(sum)