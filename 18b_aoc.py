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
        # for x in range(26):
        #     self.regs[chr(ord('a')+x)] = 0
        self.regs['p'] = pid
        self.rip = 0
        self.other = None

    def get(self,arg):
        if 'a'<=arg<='z':
            if arg in self.regs:
                return self.regs[arg]
            else:
                self.regs[arg] = 0
                return 0
        else:
            return int(arg)

    def process(self):
        global timesSent
        arg = program[self.rip]
        arg = arg.split()
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
                self.regs[arg[1]] =  self.get(arg[2])
        elif arg[0]=='add':
                self.regs[arg[1]] += self.get(arg[2])
        elif arg[0]=='mul':
                self.regs[arg[1]] *= self.get(arg[2])
        elif arg[0]=='mod':
                self.regs[arg[1]] %= self.get(arg[2])
        elif arg[0]=='rcv':
            if len(self.recieveQueue)>0:
                self.regs[arg[1]] = self.recieveQueue.pop()
            else:
                return -1
        elif arg[0]=='jgz':
            z = self.get(arg[1])
            if z>0:
                self.rip += self.get(arg[2])
                self.printState()
                return 0
        else:
            raise Exception("Instruction not found")

        self.printState()

        self.rip += 1
        return 0

    def printState(self):
        if self.pid==0:
            print "%2d: <%10s>"%(self.rip,program[self.rip])
            print "\t\t\t\t\t",self.regs,self.recieveQueue
        else:
            print "\t\t%2d: <%10s>"%(self.rip,program[self.rip])
            print "\t\t\t\t\t",self.regs,self.recieveQueue

import time

def solve():
    p0 = ProcessProgram(0)
    p1 = ProcessProgram(1)
    p0.other = p1
    p1.other = p0
    readyQ = [p1,p0]
    waitingQ = []
    while len(readyQ)>0:
        #time.sleep(0.01)
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
        assert len(readyQ)+len(waitingQ)==2
    print timesSent

def end():
    print timesSent
    sys.exit(0)

main()
