numsteps = 0
program = {}

def main():
    global numsteps, program
    raw_input()
    numsteps = int(raw_input().split()[-2])
    raw_input()
    try:
        while True:
            process_state()
    except EOFError:
        solve()

def process_state():
    i = raw_input().split()
    assert i[1]=="state"
    state = i[-1][:-1]
    process_value(state)
    process_value(state)
    raw_input()

def process_value(state):
    i = raw_input().split()
    assert i[-2]=="is"
    value = i[-1][:-1]
    newvalue,newmove,newstate = (raw_input().split()[-1][:-1],
                                 raw_input().split()[-1][:-1],
                                 raw_input().split()[-1][:-1])
    program[(state,value)] = (newvalue,newmove,newstate)

def solve():
    tm = TuringMachine(program)
    print tm.pgm
    for x in range(numsteps):
        tm.execute_step()
        #print (tm.state, tm.read_tape())
    print tm.infinite_tape.values().count('1')

class TuringMachine():
    """Turing Machine Emulator"""
    def __init__(self, pgm):
        self.infinite_tape = {}
        self.pgm = pgm
        self.state = 'A'
        self.cursor = 0
    def read_tape(self):
        if self.cursor in self.infinite_tape:
            return self.infinite_tape[self.cursor]
        else:
            return '0'
    def write_tape(self, symbol):
        self.infinite_tape[self.cursor] = symbol
    def execute_step(self):
        value,move,state = self.pgm[(self.state,self.read_tape())]
        self.write_tape(value)
        if move=='left':
            self.cursor += (-1)
        elif move=='right':
            self.cursor += 1
        self.state = state

main()
