programs = [chr(ord('a')+x) for x in range(16)]
partners = []
tot_spin = 0

def main():
    try:
        while True:
            i = raw_input()
            for x in i.split(','):
                process(x)
    except EOFError:
        analyse_results()

def a_spin(x):
    global programs
    l = len(programs)
    programs = programs[-x:] + programs
    programs = programs[:l]

def a_partner(a,b):
    i = programs.index(a)
    j = programs.index(b)
    a_exchange(i,j)

def a_exchange(a,b):
    k = programs[a]
    programs[a] = programs[b]
    programs[b] = k

def spin(x):
    a_spin(x)

def partner(a,b):
    pass

def exchange(a,b):
    a_exchange(a,b)

def process(inp):
    if inp[0]=='s':
        spin(int(inp[1:]))
    elif inp[0]=='x':
        a,b = map(int,inp[1:].split('/'))
        exchange(a,b)
    elif inp[0]=='p':
        a,b = inp[1],inp[3]
        partner(a,b)

def analyse_results():
    perm = [ord(x)-ord('a') for x in programs]
    # now we have list of partners and default arrangement
    # partners do not matter for even no of iterations
    # for (a,b) in partners:
    #     a_partner(a,b)
    start = range(16)
    for i in xrange(1000):
        for j in xrange(1000000):
            start = [start[x] for x in perm]
        print i/10.,"%"
    print "".join(chr(x+ord('a')) for x in start)

main()
