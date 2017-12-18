import sys

program = []
timesSent = 0

def main():
    try:
        while True:
            getinputs(raw_input())
    except EOFError:
        solve()

def getinputs(arg):
    program.append(arg)

class ProcessProgram():
    def __init__(self, pid):
        self.pid = pid
        self.regs = {}
        self.recieveQueue = []
        for x in range(26):
            self.regs[chr(ord('a')+x)] = 0
        self.regs['p'] = pid
        self.rip = 0
        self.other = None
    def process(self):
        global timesSent
        arg = program[self.rip]
        arg = arg.split()
        print arg, '\t\t', self.pid, self.rip
        if arg[0]=='snd':
            if self.pid == 1:
                timesSent += 1
            if arg[1] in self.regs:
                self.other.recieveQueue.insert(0,self.regs[arg[1]])
            else:
                self.other.recieveQueue.insert(0,int(arg[1]))
            self.rip += 1
            return 1
        elif arg[0]=='set':
            if arg[2] in self.regs:
                self.regs[arg[1]] = self.regs[arg[2]]
            else:
                self.regs[arg[1]] = int(arg[2])
        elif arg[0]=='add':
            if arg[2] in self.regs:
                self.regs[arg[1]] += self.regs[arg[2]]
            else:
                self.regs[arg[1]] += int(arg[2])
        elif arg[0]=='mul':
            if arg[2] in self.regs:
                self.regs[arg[1]] *= self.regs[arg[2]]
            else:
                self.regs[arg[1]] *= int(arg[2])
        elif arg[0]=='mod':
            if arg[2] in self.regs:
                self.regs[arg[1]] %= self.regs[arg[2]]
            else:
                self.regs[arg[1]] %= int(arg[2])
        elif arg[0]=='rcv':
            if len(self.recieveQueue)>0:
                self.regs[arg[1]] = self.recieveQueue.pop()
            else:
                self.rip += 1
                return -1
        elif arg[0]=='jgz':
            if arg[1] in self.regs:
                z = self.regs[arg[1]]
            else:
                z = int(arg[1])
            if z>0:
                if arg[2] in self.regs:
                    self.rip += self.regs[arg[2]]
                else:
                    self.rip += int(arg[2])
        self.rip += 1
        return 0

def solve():
    p0 = ProcessProgram(0)
    p1 = ProcessProgram(1)
    p0.other = p1
    p1.other = p0
    readyQ = [p0,p1]
    waitingQ = []
    while len(readyQ)>0:
        p = readyQ.pop()
        r = p.process()
        if r==-1:
            waitingQ.insert(0,p)
            continue
        if r==1:
            try:
                readyQ.append(waitingQ.pop())
            except IndexError:
                pass
        readyQ.insert(0,p)


def end():
    print timesSent
    sys.exit(0)

main()
