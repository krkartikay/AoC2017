class ProcessProgram():
    def __init__(self):
        self.regs = {"rip":0}
        self.recieveQueue = []
        for x in range(8):
            self.regs[chr(ord('a')+x)] = 0
        #self.regs['p'] = pid
        self.other = None
        self.times = 0
    def process(self):
        arg = program[self.regs['rip']]
        arg = arg.split()
        print arg, '\t\t', self.regs
        if arg[0]=='snd':
            if self.pid == 1:
                timesSent += 1
            if arg[1] in self.regs:
                self.other.recieveQueue.insert(0,self.regs[arg[1]])
            else:
                self.other.recieveQueue.insert(0,int(arg[1]))
            self.regs['rip'] += 1
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
        elif arg[0]=='sub':
            if arg[2] in self.regs:
                self.regs[arg[1]] -= self.regs[arg[2]]
            else:
                self.regs[arg[1]] -= int(arg[2])
        elif arg[0]=='mul':
            if arg[2] in self.regs:
                self.regs[arg[1]] *= self.regs[arg[2]]
            else:
                self.regs[arg[1]] *= int(arg[2])
            self.times += 1
        elif arg[0]=='mod':
            if arg[2] in self.regs:
                self.regs[arg[1]] %= self.regs[arg[2]]
            else:
                self.regs[arg[1]] %= int(arg[2])
        elif arg[0]=='rcv':
            if len(self.recieveQueue)>0:
                self.regs[arg[1]] = self.recieveQueue.pop()
            else:
                self.regs['rip'] += 1
                return -1
        elif arg[0]=='jnz':
            if arg[1] in self.regs:
                z = self.regs[arg[1]]
            else:
                z = int(arg[1])
            if z!=0:
                if arg[2] in self.regs:
                    self.regs['rip'] += self.regs[arg[2]]
                    return 0
                else:
                    self.regs['rip'] += int(arg[2])
                    return 0
        self.regs['rip'] += 1
        return 0

program = []

def main():
    try:
        while True:
            process(raw_input())
    except EOFError:
        solve()

def process(arg):
    program.append(arg)

def solve():
    p = ProcessProgram()
    #p.regs['a'] = 1
    while p.regs['rip']<len(program):
        p.process()
    print p.regs
    print p.times

main()
