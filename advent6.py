import math
f = open("adventinput.txt", "r")
lines = f.readlines()
prod = 1

#dict = {46:208, 85:1412, 75:1257, 82:1410}
#for t in [46, 85, 75, 82]:
t = 46857582
d = 208141212571410
root1 = 0.5*(t-math.sqrt(t*t-4*d))
root2 = 0.5*(t+math.sqrt(t*t-4*d))
total = math.floor(root2)-math.ceil(root1)+1
prod *= total
print(prod)