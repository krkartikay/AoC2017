def num(n,e):
    n = abs(n)
    e = abs(e)
    numsteps = 0
    if n>e:
        numsteps = n+e #e*2+(n-e)
    elif e>=n:
        numsteps = e*2 #n*2+(e-n)*2
    return numsteps

e = 0
n = 0

steps = raw_input().split(',')
numsteps = []

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
    numsteps += [num(n,e)]


print max(numsteps)
