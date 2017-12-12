e = 0
n = 0

steps = raw_input().split(',')

for step in steps:
    if step == "ne":
        n += 0.5
        e += 0.5
    elif step == "n":
        n += 1
    elif step == "nw":
        n += 0.5
        e -= 0.5
    elif step == "sw":
        n -= 0.5
        e -= 0.5
    elif step == "s":
        n -= 1
    elif step == "se":
        n -= 0.5
        e += 0.5

print "n: ",n,"e: ",e
