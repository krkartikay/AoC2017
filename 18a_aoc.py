import sys

regs = {}
lastPlayed = 0
program = []

def main():
    for x in range(26):
        regs[chr(ord('a')+x)] = 0
    try:
        while True:
            getinputs(raw_input())
    except EOFError:
        solve()

def getinputs(arg):
    program.append(arg)

def process(arg):
    global lastPlayed
    arg = arg.split()
    print arg
    if arg[0]=='snd':
        lastPlayed = regs[arg[1]]
    elif arg[0]=='set':
        if arg[2] in regs:
            regs[arg[1]] = regs[arg[2]]
        else:
            regs[arg[1]] = int(arg[2])
    elif arg[0]=='add':
        if arg[2] in regs:
            regs[arg[1]] += regs[arg[2]]
        else:
            regs[arg[1]] += int(arg[2])
    elif arg[0]=='mul':
        if arg[2] in regs:
            regs[arg[1]] *= regs[arg[2]]
        else:
            regs[arg[1]] *= int(arg[2])
    elif arg[0]=='mod':
        if arg[2] in regs:
            regs[arg[1]] %= regs[arg[2]]
        else:
            regs[arg[1]] %= int(arg[2])
    elif arg[0]=='rcv':
        if lastPlayed != 0:
            print lastPlayed
            sys.exit(0)
    elif arg[0]=='jgz':
        if regs[arg[1]]>0:
            return int(arg[2])
    return 1

def solve():
    i = 0
    while i<len(program):
        line = program[i]
        i += process(line)
main()
