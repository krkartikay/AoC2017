instructions = []

try:
    while True:
        instructions.append(int(raw_input()))
except EOFError:
    pass

def printlist(i,inst):
    for x in range(len(inst)):
        if x == i:
            print "(%d)"%inst[x],
        else:
            print inst[x],
    print ""

i = 0
j = 0
try:
    while True:
        #printlist(i,instructions)
        offset = instructions[i]
        instructions[i] += 1
        i += offset
        j += 1
except IndexError:
    print j
